from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VirtualVisitBase(BaseModel):
    patient_id: int
    doctor_id: int
    scheduled_time: datetime
    status: Optional[str] = "scheduled"
    meeting_link: Optional[str] = None
    notes: Optional[str] = None

class VirtualVisitCreate(VirtualVisitBase):
    pass

class VirtualVisitResponse(VirtualVisitBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class ChatLogBase(BaseModel):
    virtual_visit_id: int
    sender_id: int
    message: str
    timestamp: Optional[datetime] = None

class ChatLogCreate(ChatLogBase):
    pass

class ChatLogResponse(ChatLogBase):
    id: int
    class Config:
        from_attributes = True

class VideoSessionBase(BaseModel):
    virtual_visit_id: int
    session_id: str
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    recording_url: Optional[str] = None

class VideoSessionCreate(VideoSessionBase):
    pass

class VideoSessionResponse(VideoSessionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True 