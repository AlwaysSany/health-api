from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NotificationBase(BaseModel):
    user_id: int
    message: str
    is_read: Optional[bool] = False

class NotificationCreate(NotificationBase):
    pass

class NotificationResponse(NotificationBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class ReminderBase(BaseModel):
    user_id: int
    reminder_type: str
    message: str
    remind_at: datetime
    is_sent: Optional[bool] = False

class ReminderCreate(ReminderBase):
    pass

class ReminderResponse(ReminderBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True 