from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services.dashboard_service import dashboard_service
from app.database.database import get_db

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def get_dashboard_summary(db: Session = Depends(get_db)):
    return dashboard_service.get_summary(db)
