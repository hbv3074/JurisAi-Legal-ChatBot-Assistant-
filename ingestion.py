import os
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

def embed_and_save_documents():

    print("Initializing embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    print("Loading PDFs...")
    loader = PyPDFDirectoryLoader(
        r"C:\Users\Harsh\Downloads\LegalAssistant\Legal-CHATBOT-main\LEGAL-DATA"
    )
    docs = loader.load()

    print(f"Found {len(docs)} pages")

    if not docs:
        print("No documents found. Check folder path.")
        return

    print("Splitting documents...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    final_documents = text_splitter.split_documents(docs)
    print(f"Created {len(final_documents)} chunks")

    # Clean metadata (keep only filename)
    for doc in final_documents:
        if "source" in doc.metadata:
            doc.metadata["source"] = os.path.basename(doc.metadata["source"])

    print("Creating FAISS vector store...")
    vector_store = FAISS.from_documents(final_documents, embeddings)

    save_path = r"C:\Users\Harsh\Downloads\LegalAssistant\Legal-CHATBOT-main\my_vector_store"
    vector_store.save_local(save_path)

    print("Vectors saved successfully!")
    print("Ingestion complete.")

if __name__ == "__main__":
    embed_and_save_documents()