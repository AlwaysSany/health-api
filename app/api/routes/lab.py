from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.api.dependencies.database import get_async_session
from app.api.dependencies.auth import get_current_active_user
from app.schemas.lab import (
    LabOrderCreate, LabOrderResponse,
    LabResultCreate, LabResultResponse,
    DiagnosticImageCreate, DiagnosticImageResponse
)
from app.models.lab import LabOrder, LabResult, DiagnosticImage
from app.models.user import User

router = APIRouter(prefix="/lab", tags=["lab"])

# LabOrder endpoints
@router.post("/orders/", response_model=LabOrderResponse)
async def create_lab_order(order: LabOrderCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = LabOrder(**order.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/orders/", response_model=List[LabOrderResponse])
async def list_lab_orders(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(LabOrder))
    return result.scalars().all()

@router.get("/orders/{order_id}", response_model=LabOrderResponse)
async def get_lab_order(order_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(LabOrder, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Lab order not found")
    return obj

@router.put("/orders/{order_id}", response_model=LabOrderResponse)
async def update_lab_order(order_id: int, order: LabOrderCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(LabOrder, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Lab order not found")
    for k, v in order.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/orders/{order_id}")
async def delete_lab_order(order_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(LabOrder, order_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Lab order not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# LabResult endpoints
@router.post("/results/", response_model=LabResultResponse)
async def create_lab_result(result: LabResultCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = LabResult(**result.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/results/", response_model=List[LabResultResponse])
async def list_lab_results(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(LabResult))
    return result.scalars().all()

@router.get("/results/{result_id}", response_model=LabResultResponse)
async def get_lab_result(result_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(LabResult, result_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Lab result not found")
    return obj

@router.put("/results/{result_id}", response_model=LabResultResponse)
async def update_lab_result(result_id: int, result: LabResultCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(LabResult, result_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Lab result not found")
    for k, v in result.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/results/{result_id}")
async def delete_lab_result(result_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(LabResult, result_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Lab result not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# DiagnosticImage endpoints
@router.post("/images/", response_model=DiagnosticImageResponse)
async def create_diagnostic_image(image: DiagnosticImageCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = DiagnosticImage(**image.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/images/", response_model=List[DiagnosticImageResponse])
async def list_diagnostic_images(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(DiagnosticImage))
    return result.scalars().all()

@router.get("/images/{image_id}", response_model=DiagnosticImageResponse)
async def get_diagnostic_image(image_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(DiagnosticImage, image_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Diagnostic image not found")
    return obj

@router.put("/images/{image_id}", response_model=DiagnosticImageResponse)
async def update_diagnostic_image(image_id: int, image: DiagnosticImageCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(DiagnosticImage, image_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Diagnostic image not found")
    for k, v in image.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/images/{image_id}")
async def delete_diagnostic_image(image_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(DiagnosticImage, image_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Diagnostic image not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True} 