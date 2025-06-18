from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.api.dependencies.database import get_async_session
from app.api.dependencies.auth import get_current_active_user
from app.schemas.pharmacy import (
    MedicationCreate, MedicationResponse,
    PrescriptionCreate, PrescriptionResponse,
    PharmacyOrderCreate, PharmacyOrderResponse
)
from app.models.pharmacy import Medication, Prescription, PharmacyOrder
from app.models.user import User

router = APIRouter(prefix="/pharmacy", tags=["pharmacy"])

# Medication endpoints
@router.post("/medications/", response_model=MedicationResponse)
async def create_medication(med: MedicationCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = Medication(**med.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/medications/", response_model=List[MedicationResponse])
async def list_medications(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(Medication))
    return result.scalars().all()

@router.get("/medications/{med_id}", response_model=MedicationResponse)
async def get_medication(med_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(Medication, med_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Medication not found")
    return obj

@router.put("/medications/{med_id}", response_model=MedicationResponse)
async def update_medication(med_id: int, med: MedicationCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(Medication, med_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Medication not found")
    for k, v in med.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/medications/{med_id}")
async def delete_medication(med_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(Medication, med_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Medication not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# Prescription endpoints
@router.post("/prescriptions/", response_model=PrescriptionResponse)
async def create_prescription(pres: PrescriptionCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = Prescription(**pres.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/prescriptions/", response_model=List[PrescriptionResponse])
async def list_prescriptions(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(Prescription))
    return result.scalars().all()

@router.get("/prescriptions/{pres_id}", response_model=PrescriptionResponse)
async def get_prescription(pres_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(Prescription, pres_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return obj

@router.put("/prescriptions/{pres_id}", response_model=PrescriptionResponse)
async def update_prescription(pres_id: int, pres: PrescriptionCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(Prescription, pres_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Prescription not found")
    for k, v in pres.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/prescriptions/{pres_id}")
async def delete_prescription(pres_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(Prescription, pres_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Prescription not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# PharmacyOrder endpoints
@router.post("/orders/", response_model=PharmacyOrderResponse)
async def create_pharmacy_order(order: PharmacyOrderCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = PharmacyOrder(**order.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/orders/", response_model=List[PharmacyOrderResponse])
async def list_pharmacy_orders(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(PharmacyOrder))
    return result.scalars().all()

@router.get("/orders/{order_id}", response_model=PharmacyOrderResponse)
async def get_pharmacy_order(order_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(PharmacyOrder, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Pharmacy order not found")
    return obj

@router.put("/orders/{order_id}", response_model=PharmacyOrderResponse)
async def update_pharmacy_order(order_id: int, order: PharmacyOrderCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(PharmacyOrder, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Pharmacy order not found")
    for k, v in order.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/orders/{order_id}")
async def delete_pharmacy_order(order_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(PharmacyOrder, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Pharmacy order not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True} 