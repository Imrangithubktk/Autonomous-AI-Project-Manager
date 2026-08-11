from app.rag.embeddings import get_embedding_model

embeddings = get_embedding_model()

vector = embeddings.embed_query("Project Manager AI")

print("Embedding Length :", len(vector))
print("\nFirst 10 Values:\n")
print(vector[:10])