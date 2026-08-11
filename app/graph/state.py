from typing import TypedDict


class ProjectState(TypedDict):

    # User Query
    user_input: str

    # Conversation Memory Messages
    chat_messages: list

    # Intent decided by Supervisor
    intent: str

    # Dashboard & Analytics Data
    analytics: dict

    # AI Recommendations
    recommendations: str

    # RAG Response
    rag_response: str

    # Final Output
    final_response: str

    # Next Workflow Step
    next_step: str