from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate


class ProjectService:

    def create_project(self, db: Session, project: ProjectCreate):

        new_project = Project(
            project_name=project.project_name,
            owner_name=project.owner_name,
            description=project.description,
            start_date=project.start_date,
            end_date=project.end_date,
            status=project.status
        )

        db.add(new_project)
        db.commit()
        db.refresh(new_project)

        return new_project

    def get_projects(self, db: Session):
        return db.query(Project).all()

    def get_project_by_id(self, db: Session, project_id: int):
        return db.query(Project).filter(Project.id == project_id).first()

    def update_project(
        self,
        db: Session,
        project_id: int,
        project: ProjectUpdate
    ):
        db_project = db.query(Project).filter(Project.id == project_id).first()

        if not db_project:
            return None

        db_project.project_name = project.project_name
        db_project.owner_name = project.owner_name
        db_project.description = project.description
        db_project.start_date = project.start_date
        db_project.end_date = project.end_date
        db_project.status = project.status

        db.commit()
        db.refresh(db_project)

        return db_project

    def delete_project(self, db: Session, project_id: int):
        db_project = db.query(Project).filter(Project.id == project_id).first()

        if not db_project:
            return None

        db.delete(db_project)
        db.commit()

        return {"message": "Project deleted successfully"}


project_service = ProjectService()
