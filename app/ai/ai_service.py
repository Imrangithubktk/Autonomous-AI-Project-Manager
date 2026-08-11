from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.services.conversation_service import conversation_service

from app.models.project import Project
from app.models.task import Task
from app.ai.groq_client import get_llm
from app.graph.workflow import graph


class AIService:

    def get_ai_recommendations(self, db: Session):

        total_projects = db.query(Project).count()

        active_projects = (
            db.query(Project)
            .filter(Project.status == "Active")
            .count()
        )

        completed_projects = (
            db.query(Project)
            .filter(Project.status == "Completed")
            .count()
        )

        total_tasks = db.query(Task).count()

        pending_tasks = (
            db.query(Task)
            .filter(Task.status == "Pending")
            .count()
        )

        high_priority = (
            db.query(Task)
            .filter(
                Task.priority == "High",
                Task.status != "Completed"
            )
            .count()
        )

        overdue_tasks = (
            db.query(Task)
            .filter(Task.status == "Overdue")
            .count()
        )

        prompt = f"""
You are an AI Engineering Project Manager.

Analyze this project data and provide professional recommendations.

Project Summary:

Total Projects: {total_projects}
Active Projects: {active_projects}
Completed Projects: {completed_projects}

Total Tasks: {total_tasks}
Pending Tasks: {pending_tasks}
High Priority Tasks: {high_priority}
Overdue Tasks: {overdue_tasks}

Give only 5 short actionable recommendations.
"""

        llm = get_llm()

        response = llm.invoke(prompt)

        return {
            "status": "success",
            "recommendations": response.content
        }

    def run_workflow(self, session_id: str, user_input: str):

        db = SessionLocal()

        try:

            # Save User Message
            conversation_service.save_message(
                db=db,
                session_id=session_id,
                role="user",
                message=user_input
            )

            # Load Previous Conversation History
            # Load Previous Conversation Messages
            chat_messages = conversation_service.build_chat_messages(
            db=db,
            session_id=session_id,
            limit=10
            )

            print("\n===== CHAT MESSAGES =====")
            print(chat_messages)

            initial_state = {
            "user_input": user_input,
            "chat_messages": chat_messages,
            "intent": "",
            "analytics": {},
            "recommendations": [],
            "rag_response": "",
            "final_response": "",
            "next_step": ""
        }

            config = {
                "configurable": {
                    "thread_id": session_id
                }
            }

            result = graph.invoke(
                initial_state,
                config=config
            )

            # Save AI Response
            conversation_service.save_message(
                db=db,
                session_id=session_id,
                role="assistant",
                message=result["final_response"]
            )

            return result

        finally:
            db.close()


ai_service = AIService()