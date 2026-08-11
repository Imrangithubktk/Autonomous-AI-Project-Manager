from app.monitoring.logger import logger
from app.graph.state import ProjectState
from app.ai.groq_client import get_llm


def supervisor_agent(state: ProjectState):
    logger.info("Supervisor Agent Started")
    
    print("Supervisor Agent Running...")

    user_input = state["user_input"]

    prompt = f"""
You are an AI Supervisor Agent.

Your job is to classify the user's request.

Choose ONLY ONE of these intents:

dashboard
analytics
project_status
recommendation
rag
general

Return ONLY the intent name.

User Request:
{user_input}
"""

    llm = get_llm()

    response = llm.invoke(prompt)

    intent = response.content.strip().lower()

    valid_intents = [
        "dashboard",
        "analytics",
        "project_status",
        "recommendation",
        "rag",
        "general",
    ]

    if intent not in valid_intents:
        intent = "general"

    state["intent"] = intent
    
    logger.info(f"Intent Detected: {intent}")

    print("Supervisor Decision:", intent)
    
    logger.info("Supervisor Agent Completed")
    return state