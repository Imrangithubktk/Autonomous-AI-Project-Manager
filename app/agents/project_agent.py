from app.graph.state import ProjectState
from app.database.database import SessionLocal
from app.models.project import Project


def project_agent(state: ProjectState):

    print("Project Agent Running...")

    db = SessionLocal()

    try:

        total_projects = db.query(Project).count()

        active_projects = (
            db.query(Project)
            .filter(Project.status == "Active")
            .count()
        )

        completed_projects = (
            db.query(Project)
            .filter(Project.status == "Completed")
            .count()
        )

        state["analytics"]["projects"] = {
            "total_projects": total_projects,
            "active_projects": active_projects,
            "completed_projects": completed_projects,
        }

    finally:
        db.close()

    return state