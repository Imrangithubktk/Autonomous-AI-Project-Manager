from pydantic import BaseModel
from datetime import date

class ProjectCreate(BaseModel):
    project_name: str
    owner_name: str
    description: str
    start_date: date
    end_date: date
    status: str = "Active"
class ProjectUpdate(BaseModel):
    project_name: str
    owner_name: str
    description: str
    start_date: date
    end_date: date
    status: str
