from app.monitoring.logger import logger
from app.graph.state import ProjectState
from app.ai.groq_client import get_llm


def recommendation_agent(state: ProjectState):

    logger.info("Recommendation Agent Started")

    print("Recommendation Agent Running...")

    try:

        analytics = state.get("analytics", {})

        # -----------------------------
        # Check Analytics
        # -----------------------------

        if not analytics:

            logger.warning("Analytics data not found.")

            state["recommendations"] = (
                "Analytics data is not available. "
                "Please run analytics before requesting recommendations."
            )

            logger.info("Recommendation Agent Completed")

            return state

        dashboard = analytics.get("dashboard", {})
        project_status = analytics.get("project_status", {})
        task_status = analytics.get("task_status", {})
        task_priority = analytics.get("task_priority", {})
        deadlines = analytics.get("upcoming_deadlines", [])

        logger.info("Preparing AI Recommendation Prompt")

        prompt = f"""
You are an Expert AI Engineering Project Manager.

Analyze the following project analytics.

Dashboard:
{dashboard}

Project Status:
{project_status}

Task Status:
{task_status}

Task Priority:
{task_priority}

Upcoming Deadlines:
{deadlines}

Give ONLY 5 short actionable recommendations.
"""

        llm = get_llm()

        response = llm.invoke(prompt)

        state["recommendations"] = response.content

        logger.info("Recommendations Generated Successfully")

    except Exception as e:

        logger.error(f"Recommendation Agent Error: {str(e)}")
        raise

    logger.info("Recommendation Agent Completed")

    return state