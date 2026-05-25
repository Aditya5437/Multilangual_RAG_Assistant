# 🌍 Multilingual Government RAG Assistant

An enterprise-style multilingual Retrieval-Augmented Generation (RAG) application built using FastAPI, Streamlit, LangChain, ChromaDB, HuggingFace multilingual embeddings, and Groq Llama 3.1.

The system allows users to upload government scheme PDFs and ask questions in multiple languages such as English, Hindi, and Marathi. The application retrieves relevant information from uploaded documents using semantic search and generates contextual answers in the user’s language.

---

# 🚀 Features

- 📄 Upload and process government PDF documents
- 🌐 Multilingual question answering support
- 🔍 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG) pipeline
- ⚡ FastAPI backend APIs
- 💬 Interactive Streamlit chat interface
- 🗂 ChromaDB vector database integration
- 🤖 Groq Llama 3.1 8B Instant integration
- 🔗 LangChain orchestration
- 📊 Basic RAG evaluation metrics
- 🧩 Modular production-style project structure

---

# 🛠 Tech Stack

## Frontend
- Streamlit

## Backend
- FastAPI
- Uvicorn

## LLM
- Groq API
- Llama 3.1 8B Instant

## Embeddings
- HuggingFace Embeddings
- `intfloat/multilingual-e5-small`

## Vector Database
- ChromaDB

## Frameworks
- LangChain
- LangChain Community
- LangChain Groq

---

# 🏗 Architecture

```text
User Uploads PDF
        ↓
PDF Processing
        ↓
Text Chunking
        ↓
Multilingual Embedding Generation
        ↓
ChromaDB Vector Storage
        ↓
User Query
        ↓
Semantic Retrieval
        ↓
Groq Llama 3.1
        ↓
Answer Generation in User Language
```

---

# 📂 Project Structure

```text
multilingual-rag-assistant/
│
├── backend/
│   ├── app.py
│   ├── rag/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   ├── vectorstore/
│   └── uploaded_pdfs/
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   ├── chroma_db/
│   └── raw_pdfs/
│
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/your-username/multilingual-rag-assistant.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run FastAPI Backend

```bash
uvicorn backend.app:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# ▶️ Run Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

# 💬 Example Queries

### English

```text
What are the benefits of PM Kisan Scheme?
```

### Hindi

```text
पीएम किसान योजना क्या है?
```

### Marathi

```text
पीएम किसान योजनेचे फायदे काय आहेत?
```

---

# 📊 Evaluation Metrics

The project includes basic RAG evaluation metrics such as:

- Retrieved Chunks Count
- Response Time
- Query Length
- Response Length
- Context Relevance Score

---

# 🔮 Future Enhancements

- OCR support for scanned PDFs
- Hybrid Search (Semantic + BM25)
- Dockerization
- Cloud Deployment
- Authentication System
- Admin Dashboard
- Source Citations
- Conversation Memory
- RAGAS Evaluation Framework

---

# 🎯 Resume Highlights

- Built multilingual enterprise-grade RAG system for government documents
- Implemented semantic retrieval using ChromaDB and multilingual embeddings
- Integrated Groq Llama 3.1 with LangChain orchestration
- Developed FastAPI backend and Streamlit frontend architecture
- Designed scalable modular AI application structure

---

# 📜 License

This project is intended for educational and portfolio purposes.
