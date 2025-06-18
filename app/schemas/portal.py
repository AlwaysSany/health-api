from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MessageBase(BaseModel):
    sender_id: int
    receiver_id: int
    content: str
    sent_at: Optional[datetime] = None

class MessageCreate(MessageBase):
    pass

class MessageResponse(MessageBase):
    id: int
    class Config:
        from_attributes = True

class EducationalResourceBase(BaseModel):
    title: str
    content: str
    url: Optional[str] = None

class EducationalResourceCreate(EducationalResourceBase):
    pass

class EducationalResourceResponse(EducationalResourceBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class FeedbackBase(BaseModel):
    user_id: int
    content: str
    rating: Optional[int] = None
    created_at: Optional[datetime] = None

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackResponse(FeedbackBase):
    id: int
    class Config:
        from_attributes = True

class SurveyBase(BaseModel):
    title: str
    description: Optional[str] = None

class SurveyCreate(SurveyBase):
    pass

class SurveyResponse(SurveyBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True 