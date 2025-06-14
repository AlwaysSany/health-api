from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class DoctorBase(BaseModel):
    first_name: str
    last_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    specialization: str
    license_number: str
    years_of_experience: Optional[int] = None
    bio: Optional[str] = None


class DoctorCreate(DoctorBase):
    pass


class DoctorUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    specialization: Optional[str] = None
    years_of_experience: Optional[int] = None
    bio: Optional[str] = None


class DoctorResponse(DoctorBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
