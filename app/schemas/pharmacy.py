from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class MedicationBase(BaseModel):
    name: str
    description: Optional[str] = None
    manufacturer: Optional[str] = None

class MedicationCreate(MedicationBase):
    pass

class MedicationResponse(MedicationBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class PrescriptionBase(BaseModel):
    patient_id: int
    doctor_id: int
    medication_id: int
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    duration: Optional[str] = None
    instructions: Optional[str] = None
    issue_date: date

class PrescriptionCreate(PrescriptionBase):
    pass

class PrescriptionResponse(PrescriptionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class PharmacyOrderBase(BaseModel):
    prescription_id: int
    order_date: date
    status: Optional[str] = "pending"
    notes: Optional[str] = None

class PharmacyOrderCreate(PharmacyOrderBase):
    pass

class PharmacyOrderResponse(PharmacyOrderBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True 