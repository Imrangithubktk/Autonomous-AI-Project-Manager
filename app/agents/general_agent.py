from app.graph.state import ProjectState
from app.ai.groq_client import get_llm
from app.monitoring.logger import logger
from langchain_core.messages import SystemMessage
from langchain_core.messages import SystemMessage, HumanMessage
def general_agent(state: ProjectState):
    
    logger.info("General Agent Started")
    print("General Agent Running...")
    llm = get_llm()
    history = state.get("chat_messages") or []
    messages = [
        SystemMessage(
            content="""
You are a helpful AI Assistant.
Always use the previous conversation to answer the user.
If the answer exists in the conversation history,
never say:
- I don't know.
- This conversation just started.
- You haven't told me.
Use memory first.
If the information does not exist,
then answer normally.
"""
        )
    ]
    messages.extend(history)
    messages.append(
        HumanMessage(
            content=state["user_input"]
        )
    )
    response = llm.invoke(messages)
    state["final_response"] = response.content
    logger.info("General Agent Completed")
    return state
