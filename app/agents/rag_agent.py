from app.monitoring.logger import logger
from app.graph.state import ProjectState
from app.rag.rag_chain import ask_rag


def rag_agent(state: ProjectState):

    logger.info("RAG Agent Started")

    print("RAG Agent Running...")

    try:

        question = state.get("user_input", "")

        logger.info(
            f"RAG Query Received: {question}"
        )


        chat_messages = state.get(
            "chat_messages",
            []
        )


        answer = ask_rag(
            question,
            chat_messages
        )


        state["final_response"] = answer


        logger.info(
            "RAG Response Generated Successfully"
        )


    except Exception as e:

        logger.error(
            f"RAG Agent Error: {str(e)}"
        )

        raise


    logger.info("RAG Agent Completed")

    return state