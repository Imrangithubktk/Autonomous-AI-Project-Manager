from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():
    """
    Load HuggingFace Embedding Model
    """

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings