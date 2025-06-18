from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.api.dependencies.database import get_async_session
from app.api.dependencies.auth import get_current_active_user
from app.schemas.insurance import (
    InsurancePlanCreate, InsurancePlanResponse,
    InsuranceClaimCreate, InsuranceClaimResponse,
    PaymentCreate, PaymentResponse,
    InvoiceCreate, InvoiceResponse
)
from app.models.insurance import InsurancePlan, InsuranceClaim, Payment, Invoice
from app.models.user import User

router = APIRouter(prefix="/insurance", tags=["insurance"])

# Insurance Plans
@router.post("/plans/", response_model=InsurancePlanResponse)
async def create_insurance_plan(
    plan: InsurancePlanCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = InsurancePlan(**plan.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/plans/", response_model=List[InsurancePlanResponse])
async def list_insurance_plans(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    result = await db.execute(select(InsurancePlan).offset(skip).limit(limit))
    return result.scalars().all()

@router.get("/plans/{plan_id}", response_model=InsurancePlanResponse)
async def get_insurance_plan(
    plan_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(InsurancePlan, plan_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Insurance plan not found")
    return obj

@router.put("/plans/{plan_id}", response_model=InsurancePlanResponse)
async def update_insurance_plan(
    plan_id: int,
    plan: InsurancePlanCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(InsurancePlan, plan_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Insurance plan not found")
    for k, v in plan.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/plans/{plan_id}")
async def delete_insurance_plan(
    plan_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(InsurancePlan, plan_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Insurance plan not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# Insurance Claims
@router.post("/claims/", response_model=InsuranceClaimResponse)
async def create_insurance_claim(
    claim: InsuranceClaimCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = InsuranceClaim(**claim.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/claims/", response_model=List[InsuranceClaimResponse])
async def list_insurance_claims(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    result = await db.execute(select(InsuranceClaim).offset(skip).limit(limit))
    return result.scalars().all()

@router.get("/claims/{claim_id}", response_model=InsuranceClaimResponse)
async def get_insurance_claim(
    claim_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(InsuranceClaim, claim_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Insurance claim not found")
    return obj

@router.put("/claims/{claim_id}", response_model=InsuranceClaimResponse)
async def update_insurance_claim(
    claim_id: int,
    claim: InsuranceClaimCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(InsuranceClaim, claim_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Insurance claim not found")
    for k, v in claim.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/claims/{claim_id}")
async def delete_insurance_claim(
    claim_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(InsuranceClaim, claim_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Insurance claim not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# Payments
@router.post("/payments/", response_model=PaymentResponse)
async def create_payment(
    payment: PaymentCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = Payment(**payment.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/payments/", response_model=List[PaymentResponse])
async def list_payments(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    result = await db.execute(select(Payment).offset(skip).limit(limit))
    return result.scalars().all()

@router.get("/payments/{payment_id}", response_model=PaymentResponse)
async def get_payment(
    payment_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(Payment, payment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Payment not found")
    return obj

@router.put("/payments/{payment_id}", response_model=PaymentResponse)
async def update_payment(
    payment_id: int,
    payment: PaymentCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(Payment, payment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Payment not found")
    for k, v in payment.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/payments/{payment_id}")
async def delete_payment(
    payment_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(Payment, payment_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Payment not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# Invoices
@router.post("/invoices/", response_model=InvoiceResponse)
async def create_invoice(
    invoice: InvoiceCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = Invoice(**invoice.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/invoices/", response_model=List[InvoiceResponse])
async def list_invoices(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    result = await db.execute(select(Invoice).offset(skip).limit(limit))
    return result.scalars().all()

@router.get("/invoices/{invoice_id}", response_model=InvoiceResponse)
async def get_invoice(
    invoice_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(Invoice, invoice_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return obj

@router.put("/invoices/{invoice_id}", response_model=InvoiceResponse)
async def update_invoice(
    invoice_id: int,
    invoice: InvoiceCreate,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(Invoice, invoice_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Invoice not found")
    for k, v in invoice.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/invoices/{invoice_id}")
async def delete_invoice(
    invoice_id: int,
    db: AsyncSession = Depends(get_async_session),
    current_user: User = Depends(get_current_active_user),
):
    obj = await db.get(Invoice, invoice_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Invoice not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True} 