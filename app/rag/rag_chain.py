from app.rag.retriever import get_retriever
from app.ai.groq_client import get_llm


def ask_rag(
    question: str,
    chat_messages=None
):

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    memory = ""

    if chat_messages:

        for message in chat_messages:

            memory += (
                f"{message.type}: {message.content}\n"
            )


    prompt = f"""
You are an AI Project Manager with conversation memory.

Use the following sources:

1. Previous Conversation Memory
2. Document Context

Rules:

- Use memory when the user refers to previous conversation.
- Use documents when information exists in documents.
- If information is unavailable in both places,
  reply:
  "I couldn't find that information."

Previous Conversation:
{memory}


Document Context:
{context}


Current Question:
{question}


Answer:
"""


    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content