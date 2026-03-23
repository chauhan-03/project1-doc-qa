import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
import tempfile
import os

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Smart Document Q&A Bot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Smart Document Q&A Bot")
st.markdown("**Upload any PDF and ask questions about it using AI.**")
st.markdown("---")

# ─── Sidebar ────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Configuration")
    groq_api_key = st.text_input(
        "Groq API Key (Free)",
        type="password",
        help="Get free API key at console.groq.com"
    )
    st.markdown("[Get Free Groq API Key →](https://console.groq.com)")
    st.markdown("---")
    st.markdown("**Built by:** Jatin Chauhan")
    st.markdown("**Tech Stack:** LangChain · FAISS · HuggingFace · Groq")

# ─── File Upload ─────────────────────────────────────────────────────────────
uploaded_file = st.file_uploader("📄 Upload a PDF document", type="pdf")

if uploaded_file and groq_api_key:
    with st.spinner("🔍 Processing document..."):

        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Load and split
        loader = PyPDFLoader(tmp_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )
        chunks = splitter.split_documents(documents)

        # Embeddings + Vector Store
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        vectorstore = FAISS.from_documents(chunks, embeddings)

        # LLM
        llm = ChatGroq(
            groq_api_key=groq_api_key,
            model_name="llama3-8b-8192",
            temperature=0.2
        )

        # QA Chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )

        os.unlink(tmp_path)
        st.success(f"✅ Document processed! {len(chunks)} chunks indexed.")

    # ─── Chat Interface ──────────────────────────────────────────────────────
    st.markdown("### 💬 Ask a Question")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask anything about your document..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                result = qa_chain({"query": prompt})
                answer = result["result"]
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

elif uploaded_file and not groq_api_key:
    st.warning("⚠️ Please enter your Groq API key in the sidebar.")
else:
    st.info("👆 Upload a PDF and enter your API key to get started.")

    st.markdown("### 💡 Example Use Cases")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("📋 **Research Papers**\nAsk about findings & methodology")
    with col2:
        st.markdown("📜 **Legal Documents**\nExtract key clauses & terms")
    with col3:
        st.markdown("📊 **Reports**\nSummarize insights quickly")
