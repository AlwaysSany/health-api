from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base import Base

class VirtualVisit(Base):
    __tablename__ = "virtual_visits"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    scheduled_time = Column(DateTime(timezone=True), nullable=False)
    status = Column(String(50), default="scheduled")
    meeting_link = Column(String(255))
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ChatLog(Base):
    __tablename__ = "chat_logs"
    id = Column(Integer, primary_key=True, index=True)
    virtual_visit_id = Column(Integer, ForeignKey("virtual_visits.id"), nullable=False)
    sender_id = Column(Integer, nullable=False)  # Could be patient or doctor
    message = Column(Text)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class VideoSession(Base):
    __tablename__ = "video_sessions"
    id = Column(Integer, primary_key=True, index=True)
    virtual_visit_id = Column(Integer, ForeignKey("virtual_visits.id"), nullable=False)
    session_id = Column(String(255), nullable=False)
    started_at = Column(DateTime(timezone=True))
    ended_at = Column(DateTime(timezone=True))
    recording_url = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 