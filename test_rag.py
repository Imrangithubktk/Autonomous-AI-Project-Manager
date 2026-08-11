from app.rag.rag_chain import ask_rag

question = "What is the capital of Pakistan?"

answer = ask_rag(question)

print("\nQuestion:\n")
print(question)

print("\nAnswer:\n")
print(answer)