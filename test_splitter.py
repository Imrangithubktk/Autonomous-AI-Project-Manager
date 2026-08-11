from app.rag.loader import load_documents
from app.rag.splitter import split_documents

docs = load_documents()

chunks = split_documents(docs)

print("Total Documents :", len(docs))
print("Total Chunks    :", len(chunks))

print("\nFirst Chunk:\n")

print(chunks[0].page_content)