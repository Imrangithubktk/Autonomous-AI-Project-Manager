from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, nullable=False)
    description = Column(Text)
    priority = Column(String, nullable=False)
    status = Column(String, nullable=False)
    due_date = Column(Date)

    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship(
    "Project",
    back_populates="tasks"
    )