from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.task import TaskCreate, TaskUpdate
from app.services.task_service import task_service

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.get("/")
def get_tasks(db: Session = Depends(get_db)):
    return task_service.get_tasks(db)


@router.get("/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task_by_id(db, task_id)

    if not task:
        return {"message": "Task not found"}

    return task


@router.post("/")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    return task_service.create_task(db, task)


@router.put("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db)
):
    updated_task = task_service.update_task(db, task_id, task)

    if not updated_task:
        return {"message": "Task not found"}

    return updated_task


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    deleted_task = task_service.delete_task(db, task_id)

    if not deleted_task:
        return {"message": "Task not found"}

    return deleted_task