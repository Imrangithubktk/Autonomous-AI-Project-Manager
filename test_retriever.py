from app.rag.retriever import get_retriever

retriever = get_retriever()

docs = retriever.invoke("What is the company policy?")

print("Retrieved Documents:", len(docs))

print("\nFirst Result:\n")

print(docs[0].page_content)