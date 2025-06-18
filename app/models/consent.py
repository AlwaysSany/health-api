from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base import Base

class ConsentForm(Base):
    __tablename__ = "consent_forms"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ConsentHistory(Base):
    __tablename__ = "consent_history"
    id = Column(Integer, primary_key=True, index=True)
    consent_form_id = Column(Integer, ForeignKey("consent_forms.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    given = Column(Boolean, default=False)
    given_at = Column(DateTime(timezone=True))
    revoked = Column(Boolean, default=False)
    revoked_at = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 