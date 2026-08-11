from app.monitoring.logger import logger
from app.graph.state import ProjectState

from app.database.database import SessionLocal
from app.services.dashboard_service import dashboard_service
from app.services.analytics_service import analytics_service


def analytics_agent(state: ProjectState):

    logger.info("Analytics Agent Started")

    print("Analytics Agent Running...")

    db = SessionLocal()

    try:

        # -----------------------------
        # Fetch Dashboard Data
        # -----------------------------

        dashboard = dashboard_service.get_summary(db)

        project_status = analytics_service.project_status_summary(db)

        task_status = analytics_service.task_status_summary(db)

        task_priority = analytics_service.task_priority_summary(db)

        deadlines = analytics_service.upcoming_deadlines(db)

        # -----------------------------
        # Store Analytics
        # -----------------------------

        state["analytics"] = {
            "dashboard": dashboard,
            "project_status": project_status,
            "task_status": task_status,
            "task_priority": task_priority,
            "upcoming_deadlines": deadlines
        }

        logger.info("Dashboard Summary Generated")
        logger.info(f"Dashboard: {dashboard}")
        logger.info(f"Project Status: {project_status}")
        logger.info(f"Task Status: {task_status}")
        logger.info(f"Task Priority: {task_priority}")
        logger.info(f"Upcoming Deadlines: {len(deadlines)}")

        # -----------------------------
        # Decide Next Step
        # -----------------------------

        if state["intent"] == "recommendation":

            state["next_step"] = "recommendation"

        else:

            state["next_step"] = "reporter"

        logger.info(f"Next Step: {state['next_step']}")

    except Exception as e:

        logger.error(f"Analytics Agent Error: {str(e)}")
        raise

    finally:

        db.close()

    print(state["analytics"])
    print("Next Step:", state["next_step"])

    logger.info("Analytics Agent Completed")

    return state