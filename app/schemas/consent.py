from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ConsentFormBase(BaseModel):
    title: str
    content: str

class ConsentFormCreate(ConsentFormBase):
    pass

class ConsentFormResponse(ConsentFormBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class ConsentHistoryBase(BaseModel):
    consent_form_id: int
    user_id: int
    given: Optional[bool] = False
    given_at: Optional[datetime] = None
    revoked: Optional[bool] = False
    revoked_at: Optional[datetime] = None

class ConsentHistoryCreate(ConsentHistoryBase):
    pass

class ConsentHistoryResponse(ConsentHistoryBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True 