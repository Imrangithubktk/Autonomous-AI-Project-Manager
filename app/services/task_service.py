from sqlalchemy.orm import Session

from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:

    def create_task(self, db: Session, task: TaskCreate):

        new_task = Task(
            task_name=task.task_name,
            description=task.description,
            priority=task.priority,
            status=task.status,
            due_date=task.due_date,
            project_id=task.project_id
        )

        db.add(new_task)
        db.commit()
        db.refresh(new_task)

        return new_task

    def get_tasks(self, db: Session):
        return db.query(Task).all()

    def get_task_by_id(self, db: Session, task_id: int):
        return db.query(Task).filter(Task.id == task_id).first()

    def update_task(
        self,
        db: Session,
        task_id: int,
        task: TaskUpdate
    ):
        db_task = db.query(Task).filter(Task.id == task_id).first()

        if not db_task:
            return None

        db_task.task_name = task.task_name
        db_task.description = task.description
        db_task.priority = task.priority
        db_task.status = task.status
        db_task.due_date = task.due_date
        db_task.project_id = task.project_id

        db.commit()
        db.refresh(db_task)

        return db_task

    def delete_task(self, db: Session, task_id: int):
        db_task = db.query(Task).filter(Task.id == task_id).first()

        if not db_task:
            return None

        db.delete(db_task)
        db.commit()

        return {"message": "Task deleted successfully"}


task_service = TaskService()