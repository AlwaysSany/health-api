from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base import Base

class ReferralRequest(Base):
    __tablename__ = "referral_requests"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    referring_doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    specialist_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    request_date = Column(Date, nullable=False)
    reason = Column(Text)
    status_id = Column(Integer, ForeignKey("referral_statuses.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ReferralStatus(Base):
    __tablename__ = "referral_statuses"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class SpecialistNote(Base):
    __tablename__ = "specialist_notes"
    id = Column(Integer, primary_key=True, index=True)
    referral_request_id = Column(Integer, ForeignKey("referral_requests.id"), nullable=False)
    note = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 