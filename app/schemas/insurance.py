from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List

class InsurancePlanBase(BaseModel):
    name: str
    provider: str
    coverage_details: Optional[str] = None

class InsurancePlanCreate(InsurancePlanBase):
    pass

class InsurancePlanResponse(InsurancePlanBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class InsuranceClaimBase(BaseModel):
    patient_id: int
    plan_id: int
    claim_date: date
    amount: float
    status: Optional[str] = "pending"
    details: Optional[str] = None

class InsuranceClaimCreate(InsuranceClaimBase):
    pass

class InsuranceClaimResponse(InsuranceClaimBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class PaymentBase(BaseModel):
    patient_id: int
    amount: float
    payment_date: date
    method: Optional[str] = None
    invoice_id: Optional[int] = None

class PaymentCreate(PaymentBase):
    pass

class PaymentResponse(PaymentBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class InvoiceBase(BaseModel):
    patient_id: int
    total_amount: float
    issue_date: date
    due_date: Optional[date] = None
    status: Optional[str] = "unpaid"
    details: Optional[str] = None

class InvoiceCreate(InvoiceBase):
    pass

class InvoiceResponse(InvoiceBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True 