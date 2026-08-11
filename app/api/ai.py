from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.database import get_db
from app.ai.ai_service import ai_service


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


class ChatRequest(BaseModel):

    session_id: str
    message: str



@router.post("/chat")
def ai_chat(request: ChatRequest):

    result = ai_service.run_workflow(
        request.session_id,
        request.message
    )

    return result



@router.get("/recommendations")
def get_recommendations(
    db: Session = Depends(get_db)
):

    return ai_service.get_ai_recommendations(db)