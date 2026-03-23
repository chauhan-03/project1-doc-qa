# 🤖 Smart Document Q&A Bot

An AI-powered document assistant that lets you **upload any PDF and ask questions about it** using Retrieval Augmented Generation (RAG).

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.1.16-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-orange)
![Groq](https://img.shields.io/badge/Groq-LLaMA3-purple)

---

## 🚀 Live Demo
[👉 Click here to try it live](#) *(Deploy on Streamlit Cloud — free)*

---

## 🧠 How It Works

```
PDF Upload → Text Extraction → Chunking → Embeddings (HuggingFace)
     → FAISS Vector Store → Groq LLaMA3 LLM → Answer
```

| Step | Technology |
|---|---|
| PDF Parsing | PyPDF |
| Text Chunking | LangChain RecursiveTextSplitter |
| Embeddings | HuggingFace all-MiniLM-L6-v2 |
| Vector Search | FAISS |
| LLM | Groq (LLaMA3-8B) — Free API |
| UI | Streamlit |

---

## 📁 Project Structure

```
project1-doc-qa/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Dependencies
└── README.md           # This file
```

---

## ⚙️ Setup & Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/chauhan-03/smart-doc-qa-bot
cd smart-doc-qa-bot

# 2. Install dependencies
pip install -r requirements.txt

# 3. Get free Groq API key
# Visit: https://console.groq.com → Sign up → Create API Key

# 4. Run the app
streamlit run app.py
```

---

## 🌐 Deploy for Free (Streamlit Cloud)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repo → Deploy
4. Add `GROQ_API_KEY` in secrets

---

## 💡 Use Cases

- 📋 Ask questions about research papers
- 📜 Extract key info from legal documents
- 📊 Summarize long business reports
- 🎓 Study from textbooks interactively

---

## 👨‍💻 Author

**Jatin Chauhan** — Engineer at Samsung R&D
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/jatin-chauhan-a07153171/)
