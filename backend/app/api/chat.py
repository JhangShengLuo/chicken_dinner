from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_user
from app.models.user import User, ChatHistory
from app.schemas.chat import ChatRequest, ChatResponse
from app.ai.agent import create_agent
from datetime import datetime
import uuid

router = APIRouter()

@router.post("/message", response_model=ChatResponse)
def send_message(request: ChatRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        session_id = str(uuid.uuid4())

        user_msg = ChatHistory(
            user_id=current_user.id,
            session_id=session_id,
            message_role="user",
            message_content=request.message,
            timestamp=datetime.utcnow().isoformat()
        )
        db.add(user_msg)
        db.commit()

        agent = create_agent(provider_name=request.provider, language=request.language)

        try:
            response_text = agent.invoke({"input": request.message}).get("output", "Error processing request.")
        except Exception as e:
            print(f"Agent error: {e}")
            response_text = "I encountered an error trying to process your request."

        ai_msg = ChatHistory(
            user_id=current_user.id,
            session_id=session_id,
            message_role="assistant",
            message_content=response_text,
            timestamp=datetime.utcnow().isoformat()
        )
        db.add(ai_msg)
        db.commit()

        return {"reply": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
