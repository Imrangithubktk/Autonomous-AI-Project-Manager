from app.graph.state import ProjectState
from app.database.database import SessionLocal
from app.models.task import Task


def task_agent(state: ProjectState):

    print("Task Agent Running...")

    db = SessionLocal()

    try:

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

        high_priority_tasks = (
            db.query(Task)
            .filter(Task.priority == "High")
            .count()
        )

        state["analytics"]["tasks"] = {
            "total_tasks": total_tasks,
            "pending_tasks": pending_tasks,
            "completed_tasks": completed_tasks,
            "high_priority_tasks": high_priority_tasks,
        }

    finally:
        db.close()

    return state