from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.task import Task


class DashboardService:

    def get_summary(self, db: Session):

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

        total_tasks = db.query(Task).count()

        pending_tasks = (
            db.query(Task)
            .filter(Task.status == "Pending")
            .count()
        )

        completed_tasks = (
            db.query(Task)
            .filter(Task.status == "Completed")
            .count()
        )

        return {
            "total_projects": total_projects,
            "active_projects": active_projects,
            "completed_projects": completed_projects,
            "total_tasks": total_tasks,
            "pending_tasks": pending_tasks,
            "completed_tasks": completed_tasks
        }


dashboard_service = DashboardService()