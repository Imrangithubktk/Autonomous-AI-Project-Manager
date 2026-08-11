from app.api.task import router as task_router
from fastapi import FastAPI
from app.api.dashboard import router as dashboard_router
from app.api.analytics import router as analytics_router
from app.api.ai import router as ai_router

from app.database.database import engine
from app.database.base import Base
import app.models

from app.api.project import router as project_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Autonomous AI Project Manager",
    version="1.0.0",
    description="AI-powered Engineering Project Management Platform"
)

app.include_router(project_router)
app.include_router(task_router)
app.include_router(dashboard_router)
app.include_router(analytics_router)
app.include_router(ai_router)



@app.get("/")
def home():
    return {
        "message": "Welcome to Autonomous AI Project Manager",
        "version": "1.0.0",
        "status": "Running Successfully"
    }