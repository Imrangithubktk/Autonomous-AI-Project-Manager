from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.database.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    owner_name = Column(String, nullable=True) 
    description = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)

    tasks = relationship(
        "Task",
        back_populates="project",
        cascade="all, delete"
    )
