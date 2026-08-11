from app.rag.loader import load_documents

docs = load_documents()

print("Total Documents:", len(docs))

print("\nFirst Document:\n")

print(docs[0].page_content)