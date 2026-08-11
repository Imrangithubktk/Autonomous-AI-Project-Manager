from langchain_community.vectorstores import FAISS
from app.rag.embeddings import get_embedding_model


def get_retriever():

    embeddings = get_embedding_model()

    vector_db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vector_db.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever