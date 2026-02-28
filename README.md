📘 JurisRAG
AI-Powered Legal Information Retrieval System
⚖️ Overview

JurisRAG is an AI-powered legal information retrieval system built using Retrieval-Augmented Generation (RAG).
It enables users to query statutory documents and receive accurate, context-grounded responses.

Instead of generating answers purely from a language model’s internal knowledge, JurisRAG retrieves relevant sections from legal documents and then generates responses grounded in that retrieved context.

This significantly reduces hallucination and improves reliability for legal domain queries.

🚀 Key Features

📄 PDF-based statutory corpus ingestion

🔍 Semantic search using FAISS vector indexing

🧠 Context-aware response generation (RAG architecture)

⚡ Fast nearest-neighbor retrieval

💬 Clean Streamlit-based interactive UI

🔐 Environment-variable based API key management

🏗️ System Architecture
1️⃣ Data Ingestion & Indexing Pipeline
PDF Loader 
   ↓
Text Extraction 
   ↓
Sliding-Window Chunking 
   ↓
Embedding Generation (MiniLM) 
   ↓
FAISS Vector Store
2️⃣ Query Processing Flow
User Query
   ↓
Query Embedding
   ↓
Top-K Semantic Retrieval
   ↓
LLM Response Generation (Groq - Llama)
   ↓
Final Context-Grounded Answer
🛠️ Technologies Used
🔹 Backend & RAG

LangChain

FAISS (Vector Database)

HuggingFace Sentence Transformers

Groq (Llama Model API)

🔹 Frontend

Streamlit

🔹 Supporting Libraries

PyPDF (PDF parsing)

Python-dotenv (environment management)

NumPy

Transformers

Torch

📚 Legal Corpus Used

The system indexes statutory documents including:

Copyright Act

Criminal Law Amendment Act 2018

Indian Penal Code

Companies Act 2013

Constitution of India

Other legal documents (PDF-based corpus)

⚙️ Installation Guide
1️⃣ Clone the Repository
git clone <your-repo-link>
cd JurisRAG
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Set API Key

Create a .env file:

GROQ_API_KEY=your_api_key_here
4️⃣ Run Ingestion Pipeline
python ingestion.py

This creates the FAISS vector store.

5️⃣ Run Application
streamlit run app.py
📂 Project Structure
JurisRAG/
│
├── app.py
├── ingestion.py
├── requirements.txt
├── .env
├── my_vector_store/
└── LEGAL-DATA/
🎯 How It Works

Legal PDFs are loaded and parsed.

Text is split using sliding-window chunking.

Each chunk is converted into embeddings using MiniLM.

Embeddings are stored in FAISS.

When a query is asked:

The query is embedded

Top relevant chunks are retrieved

Retrieved context is passed to the LLM

A grounded answer is generated

🧠 Why RAG Instead of Pure LLM?

Traditional LLMs:

May hallucinate

Lack document grounding

RAG-based systems:

Retrieve actual legal text

Reduce hallucination

Improve factual accuracy

Provide explainable answers

📌 Limitations

Depends on quality of indexed documents

Does not replace professional legal advice

Accuracy depends on chunking and retrieval strategy

🔮 Future Improvements

📤 User-uploaded document support

💾 Save chat history feature

📊 Confidence scoring for retrieved answers

🔎 Section-wise citation highlighting

🌐 Deployment on cloud infrastructure

👨‍💻 Authors

Harsh Balkrishna Vahal

Project Guide: Prof. Pallavi Nikumbh

Department of Computer Science
PCCOE

📜 License

This project is developed for academic and research purposes.
