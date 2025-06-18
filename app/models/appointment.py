from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from app.database.base import Base


class AppointmentStatusEnum(enum.Enum):
    SCHEDULED = "scheduled"
    CONFIRMED = "confirmed"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    NO_SHOW = "no_show"


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=False)
    appointment_datetime = Column(DateTime(timezone=True), nullable=False)
    duration_minutes = Column(Integer, default=30)
    status = Column(
        Enum(AppointmentStatusEnum), default=AppointmentStatusEnum.SCHEDULED
    )
    reason = Column(String(500))
    notes = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    appointment_type = Column(String(20), default="in_person")
    location = Column(String(255))
    reminder_sent = Column(Integer, default=0)
    follow_up_required = Column(Integer, default=0)

    # Relationships
    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
