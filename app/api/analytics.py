from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.analytics_service import analytics_service

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/project-status")
def project_status_summary(
    db: Session = Depends(get_db)
):
    return analytics_service.project_status_summary(db)


@router.get("/task-status")
def task_status_summary(
    db: Session = Depends(get_db)
):
    return analytics_service.task_status_summary(db)


@router.get("/task-priority")
def task_priority_summary(
    db: Session = Depends(get_db)
):
    return analytics_service.task_priority_summary(db)
@router.get("/upcoming-deadlines")
def upcoming_deadlines(
    db: Session = Depends(get_db)
):
    return analytics_service.upcoming_deadlines(db)
@router.get("/overdue")
def overdue_tasks(
    db: Session = Depends(get_db)
):
    return analytics_service.overdue_tasks(db)
@router.get("/dashboard")
def dashboard_summary(
    db: Session = Depends(get_db)
):
    return analytics_service.dashboard_summary(db)