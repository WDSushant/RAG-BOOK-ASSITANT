import os
import tempfile
import streamlit as st
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import (
    GoogleGenerativeAIEmbeddings,
    ChatGoogleGenerativeAI,
)
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("GOOGLE_API_KEY not found in .env file")
    st.stop()

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(
    page_title="📚 RAG Book Assistant",
    page_icon="📚",
)

st.title("📚 RAG Book Assistant")
st.write("Upload a PDF and ask questions from it.")

# -----------------------------
# Embedding Model
# -----------------------------
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",
    google_api_key=GOOGLE_API_KEY,
)

VECTOR_DB = "chroma_db"

# -----------------------------
# Upload PDF
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload PDF",
    type="pdf"
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    st.success("PDF Uploaded Successfully!")

    if st.button("Create Vector Database"):

        with st.spinner("Processing PDF..."):

            loader = PyPDFLoader(pdf_path)
            docs = loader.load()

            splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
            )

            chunks = splitter.split_documents(docs)

            vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=embeddings,
                persist_directory=VECTOR_DB,
            )

        st.success("Vector Database Created Successfully!")

# -----------------------------
# Load Existing Database
# -----------------------------
if os.path.exists(VECTOR_DB):

    vectorstore = Chroma(
        persist_directory=VECTOR_DB,
        embedding_function=embeddings,
    )

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 4,
            "fetch_k": 10,
            "lambda_mult": 0.5,
        },
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2,
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You are a helpful AI assistant.

Answer ONLY from the supplied context.

If the answer does not exist in the context,
reply exactly:

I could not find the answer in the document.
                """,
            ),
            (
                "human",
                """
Context:
{context}

Question:
{question}
                """,
            ),
        ]
    )

    st.divider()
    st.subheader("Ask Questions")

    query = st.text_input("Enter your question")

    if query:

        with st.spinner("Searching..."):

            docs = retriever.invoke(query)

            context = "\n\n".join(
                doc.page_content for doc in docs
            )

            messages = prompt.invoke(
                {
                    "context": context,
                    "question": query,
                }
            )

            response = llm.invoke(messages)

            st.markdown("## 🤖 Answer")
            st.write(response.content)

            with st.expander("Retrieved Chunks"):

                for i, doc in enumerate(docs, start=1):
                    st.markdown(f"### Chunk {i}")
                    st.write(doc.page_content)
                    st.divider()