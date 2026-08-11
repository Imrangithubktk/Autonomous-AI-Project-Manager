from datetime import date
from typing import Optional

from pydantic import BaseModel


class TaskCreate(BaseModel):
    task_name: str
    description: Optional[str] = None
    priority: str
    status: str
    due_date: date
    project_id: int


class TaskUpdate(BaseModel):
    task_name: str
    description: Optional[str] = None
    priority: str
    status: str
    due_date: date
    project_id: int