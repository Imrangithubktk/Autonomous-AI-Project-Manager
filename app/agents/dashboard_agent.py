from app.graph.state import ProjectState
from app.services.dashboard_service import dashboard_service
from app.database.database import SessionLocal


def dashboard_agent(state: ProjectState):

    print("Dashboard Agent Running...")

    db = SessionLocal()

    try:
        dashboard = dashboard_service.get_dashboard_summary(db)

        state["analytics"] = {
            "dashboard": dashboard
        }

    finally:
        db.close()

    return state