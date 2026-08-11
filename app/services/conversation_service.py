from sqlalchemy.orm import Session

from app.models.conversation import Conversation
from langchain_core.messages import HumanMessage, AIMessage

class ConversationService:

    def save_message(
        self,
        db: Session,
        session_id: str,
        role: str,
        message: str
    ):

        conversation = Conversation(
            session_id=session_id,
            role=role,
            message=message
        )

        db.add(conversation)
        db.commit()
        db.refresh(conversation)

        return conversation

    def get_history(
        self,
        db: Session,
        session_id: str,
        limit: int = 10
    ):

        conversations = (
            db.query(Conversation)
            .filter(
                Conversation.session_id == session_id
            )
            .order_by(Conversation.id.desc())
            .limit(limit)
            .all()
        )

        conversations.reverse()

        return conversations

    def clear_history(
        self,
        db: Session,
        session_id: str
    ):

        db.query(Conversation).filter(
            Conversation.session_id == session_id
        ).delete()

        db.commit()

    def build_chat_messages(
    self,
    db: Session,
    session_id: str,
    limit: int = 10
    ):

      history = self.get_history(
        db=db,
        session_id=session_id,
        limit=limit
      )

      messages = []

      for chat in history:

        if chat.role.lower() == "user":

            messages.append(
                HumanMessage(content=chat.message)
            )

        elif chat.role.lower() == "assistant":

            messages.append(
                AIMessage(content=chat.message)
            )

              
            return messages


conversation_service = ConversationService()