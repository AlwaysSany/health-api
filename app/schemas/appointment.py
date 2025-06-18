from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.appointment import AppointmentStatusEnum


class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_datetime: datetime
    duration_minutes: Optional[int] = 30
    reason: Optional[str] = None
    notes: Optional[str] = None
    appointment_type: Optional[str] = "in_person"
    location: Optional[str] = None
    reminder_sent: Optional[bool] = False
    follow_up_required: Optional[bool] = False


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentUpdate(BaseModel):
    appointment_datetime: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    status: Optional[AppointmentStatusEnum] = None
    reason: Optional[str] = None
    notes: Optional[str] = None
    appointment_type: Optional[str] = None
    location: Optional[str] = None
    reminder_sent: Optional[bool] = None
    follow_up_required: Optional[bool] = None


class AppointmentResponse(AppointmentBase):
    id: int
    status: AppointmentStatusEnum
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
