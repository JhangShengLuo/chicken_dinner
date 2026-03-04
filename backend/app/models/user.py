from sqlalchemy import Boolean, Column, Integer, String, Float, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    financial_profile = relationship("FinancialProfile", back_populates="user", uselist=False)
    chats = relationship("ChatHistory", back_populates="user")

class FinancialProfile(Base):
    __tablename__ = "financial_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Life Stage Info
    age = Column(Integer, nullable=True)
    marital_status = Column(String, nullable=True)
    dependents = Column(Integer, default=0)

    # Financial Info
    annual_income = Column(Float, nullable=True)
    total_savings = Column(Float, nullable=True)
    monthly_expenses = Column(Float, nullable=True)
    debts = Column(JSON, nullable=True)  # Store lists of debts

    user = relationship("User", back_populates="financial_profile")

class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    session_id = Column(String, index=True)
    message_role = Column(String) # 'user' or 'assistant'
    message_content = Column(String)
    timestamp = Column(String) # Simple ISO string for now

    user = relationship("User", back_populates="chats")
