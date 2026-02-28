import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import PromptTemplate

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="JurisAi",
    page_icon="⚖️",
    layout="centered"
)

# --- CSS BLOCK HERE ---
st.markdown("""
<style>
/* Improve main container spacing */
.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
}

/* Title styling */
h2 {
    font-weight: 700;
    letter-spacing: 0.5px;
}

/* Subtitle refinement */
[data-testid="stCaption"] {
    font-size: 14px;
    opacity: 0.8;
}

/* Divider soft look */
hr {
    opacity: 0.2;
}

/* Input box polish */
textarea {
    border-radius: 12px !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown("## ⚖️ JurisAi")
st.caption("AI-Powered Legal Information Retrieval System (RAG-Based Prototype)")

st.divider()

# ------------------ LOAD ENV ------------------
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# ------------------ SESSION STATE ------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferWindowMemory(
        memory_key="chat_history",
        return_messages=True,
        k=2
    )

# ------------------ LOAD VECTOR STORE ------------------
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = FAISS.load_local(
    r"C:\Users\Harsh\Downloads\LegalAssistant\Legal-CHATBOT-main\my_vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 10, "fetch_k": 20}
)

# ------------------ PROMPT ------------------
prompt_template = """
You are a legal assistant. Answer strictly using the provided context.
If the answer is not found in the context, respond with:
"The provided context does not contain sufficient information."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# ------------------ LLM ------------------
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="llama-3.3-70b-versatile"
)

# ------------------ CHAIN ------------------
qa = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=st.session_state.memory,
    combine_docs_chain_kwargs={"prompt": prompt}
)

# ------------------ DISPLAY CHAT ------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ------------------ INPUT ------------------
user_input = st.chat_input("Enter your legal query...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Retrieving statutory provisions..."):
            result = qa.invoke({"question": user_input})
            response = result["answer"]
            st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})

# ------------------ FOOTER ------------------
st.divider()
st.caption("Developed as an academic prototype using Retrieval-Augmented Generation (RAG).")