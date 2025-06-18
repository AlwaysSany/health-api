from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class LabOrderBase(BaseModel):
    patient_id: int
    doctor_id: int
    order_date: date
    test_type: str
    status: Optional[str] = "ordered"
    notes: Optional[str] = None

class LabOrderCreate(LabOrderBase):
    pass

class LabOrderResponse(LabOrderBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class LabResultBase(BaseModel):
    lab_order_id: int
    result_date: date
    result_data: Optional[str] = None
    status: Optional[str] = "pending"

class LabResultCreate(LabResultBase):
    pass

class LabResultResponse(LabResultBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class DiagnosticImageBase(BaseModel):
    lab_order_id: int
    image_url: str
    description: Optional[str] = None

class DiagnosticImageCreate(DiagnosticImageBase):
    pass

class DiagnosticImageResponse(DiagnosticImageBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True 