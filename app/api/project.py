from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.services.project_service import project_service

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return project_service.get_projects(db)


@router.post("/")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):
    return project_service.create_project(db, project)
@router.get("/{project_id}")
def get_project_by_id(
    project_id: int,
    db: Session = Depends(get_db)
):
    return project_service.get_project_by_id(db, project_id)
@router.put("/{project_id}")
def update_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db)
):
    updated_project = project_service.update_project(
        db,
        project_id,
        project
    )

    if not updated_project:
        return {"message": "Project not found"}

    return updated_project
@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db)
):
    deleted_project = project_service.delete_project(db, project_id)

    if not deleted_project:
        return {"message": "Project not found"}

    return deleted_project