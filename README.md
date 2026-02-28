# ⚖️ JurisRAG  
### AI-Powered Legal Information Retrieval System  

---

## 📘 Overview

**JurisRAG** is an AI-powered legal information retrieval system built using Retrieval-Augmented Generation (RAG).  
It enables users to query statutory documents and receive accurate, context-grounded responses.

Instead of relying purely on a language model’s internal knowledge, JurisRAG retrieves relevant legal sections from indexed statutory documents and generates answers grounded in that retrieved context. This significantly reduces hallucination and improves reliability in the legal domain.

---

## 🚀 Key Features

- 📄 PDF-based statutory corpus ingestion  
- 🔍 Semantic search using FAISS vector indexing  
- 🧠 Context-aware response generation (RAG architecture)  
- ⚡ Fast nearest-neighbor retrieval  
- 💬 Clean Streamlit-based interactive UI  
- 🔐 Secure API key management via environment variables  

---

## 🏗️ System Architecture

### 1️⃣ Data Ingestion & Indexing Pipeline

```
PDF Loader  
   ↓  
Text Extraction  
   ↓  
Sliding-Window Chunking  
   ↓  
Embedding Generation (MiniLM)  
   ↓  
FAISS Vector Store  
```

### 2️⃣ Query Processing Flow

```
User Query  
   ↓  
Query Embedding  
   ↓  
Top-K Semantic Retrieval  
   ↓  
LLM Response Generation (Groq - Llama Model)  
   ↓  
Final Context-Grounded Answer  
```

---

## 🛠️ Technologies Used

### 🔹 Backend & RAG
- LangChain  
- FAISS (Vector Database)  
- HuggingFace Sentence Transformers  
- Groq (Llama Model API)  

### 🔹 Frontend
- Streamlit  

### 🔹 Supporting Libraries
- PyPDF  
- Python-dotenv  
- NumPy  
- Transformers  
- Torch  

---

## 📚 Legal Corpus Indexed

The system indexes statutory documents including:

- Copyright Act  
- Criminal Law Amendment Act 2018  
- Indian Penal Code  
- Companies Act 2013  
- Constitution of India  
- Additional legal PDF documents  

---

## ⚙️ Installation Guide

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-link>
cd JurisRAG
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

### 4️⃣ Run the Ingestion Pipeline

```bash
python ingestion.py
```

This generates the FAISS vector store from the legal corpus.

### 5️⃣ Launch the Application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
JurisRAG/
│
├── app.py
├── ingestion.py
├── requirements.txt
├── .env
├── my_vector_store/
└── LEGAL-DATA/
```

---

## 🎯 How It Works

1. Legal PDFs are loaded and parsed.
2. Text is split using sliding-window chunking.
3. Each chunk is converted into embeddings using MiniLM.
4. Embeddings are stored in a FAISS vector index.
5. When a user query is submitted:
   - The query is embedded
   - Top relevant chunks are retrieved
   - Retrieved context is passed to the LLM
   - A grounded answer is generated

---

## 🧠 Why RAG Instead of Pure LLM?

Traditional LLM-based systems:
- May hallucinate
- Lack document grounding
- Cannot verify source relevance

RAG-based systems:
- Retrieve actual legal text
- Reduce hallucination
- Improve factual accuracy
- Provide explainable, context-backed responses

---

## 📌 Limitations

- Dependent on quality and completeness of indexed documents  
- Does not replace professional legal consultation  
- Retrieval accuracy depends on chunking and embedding strategy  

---

## 🔮 Future Improvements

- 📤 User-uploaded document support  
- 💾 Save chat history feature  
- 📊 Confidence scoring for responses  
- 🔎 Section-wise citation highlighting  
- ☁️ Cloud deployment (Docker / AWS / GCP)  

---

## 👨‍💻 Authors

- Harsh Balkrishna Vahal   

---

## 📜 License

This project is developed for academic and research purposes.
