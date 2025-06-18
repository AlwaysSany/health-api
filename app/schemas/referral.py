from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ReferralRequestBase(BaseModel):
    patient_id: int
    referring_doctor_id: int
    specialist_id: int
    request_date: date
    reason: Optional[str] = None
    status_id: Optional[int] = None

class ReferralRequestCreate(ReferralRequestBase):
    pass

class ReferralRequestResponse(ReferralRequestBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class ReferralStatusBase(BaseModel):
    status: str
    description: Optional[str] = None

class ReferralStatusCreate(ReferralStatusBase):
    pass

class ReferralStatusResponse(ReferralStatusBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class SpecialistNoteBase(BaseModel):
    referral_request_id: int
    note: str

class SpecialistNoteCreate(SpecialistNoteBase):
    pass

class SpecialistNoteResponse(SpecialistNoteBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True 