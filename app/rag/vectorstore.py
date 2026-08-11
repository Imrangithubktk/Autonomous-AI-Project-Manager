from langchain_community.vectorstores import FAISS

from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import get_embedding_model


def create_vector_store():

    documents = load_documents()

    chunks = split_documents(documents)

    embeddings = get_embedding_model()

    vector_db = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_db.save_local("faiss_index")

    return vector_db