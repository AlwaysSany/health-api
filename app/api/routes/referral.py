from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.api.dependencies.database import get_async_session
from app.api.dependencies.auth import get_current_active_user
from app.schemas.referral import (
    ReferralRequestCreate, ReferralRequestResponse,
    ReferralStatusCreate, ReferralStatusResponse,
    SpecialistNoteCreate, SpecialistNoteResponse
)
from app.models.referral import ReferralRequest, ReferralStatus, SpecialistNote
from app.models.user import User

router = APIRouter(prefix="/referral", tags=["referral"])

# ReferralRequest endpoints
@router.post("/requests/", response_model=ReferralRequestResponse)
async def create_referral_request(req: ReferralRequestCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = ReferralRequest(**req.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/requests/", response_model=List[ReferralRequestResponse])
async def list_referral_requests(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(ReferralRequest))
    return result.scalars().all()

@router.get("/requests/{req_id}", response_model=ReferralRequestResponse)
async def get_referral_request(req_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(ReferralRequest, req_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Referral request not found")
    return obj

@router.put("/requests/{req_id}", response_model=ReferralRequestResponse)
async def update_referral_request(req_id: int, req: ReferralRequestCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(ReferralRequest, req_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Referral request not found")
    for k, v in req.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/requests/{req_id}")
async def delete_referral_request(req_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(ReferralRequest, req_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Referral request not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# ReferralStatus endpoints
@router.post("/statuses/", response_model=ReferralStatusResponse)
async def create_referral_status(status_obj: ReferralStatusCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = ReferralStatus(**status_obj.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/statuses/", response_model=List[ReferralStatusResponse])
async def list_referral_statuses(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(ReferralStatus))
    return result.scalars().all()

@router.get("/statuses/{status_id}", response_model=ReferralStatusResponse)
async def get_referral_status(status_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(ReferralStatus, status_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Referral status not found")
    return obj

@router.put("/statuses/{status_id}", response_model=ReferralStatusResponse)
async def update_referral_status(status_id: int, status_obj: ReferralStatusCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(ReferralStatus, status_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Referral status not found")
    for k, v in status_obj.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/statuses/{status_id}")
async def delete_referral_status(status_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(ReferralStatus, status_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Referral status not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# SpecialistNote endpoints
@router.post("/notes/", response_model=SpecialistNoteResponse)
async def create_specialist_note(note: SpecialistNoteCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = SpecialistNote(**note.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/notes/", response_model=List[SpecialistNoteResponse])
async def list_specialist_notes(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(SpecialistNote))
    return result.scalars().all()

@router.get("/notes/{note_id}", response_model=SpecialistNoteResponse)
async def get_specialist_note(note_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(SpecialistNote, note_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Specialist note not found")
    return obj

@router.put("/notes/{note_id}", response_model=SpecialistNoteResponse)
async def update_specialist_note(note_id: int, note: SpecialistNoteCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(SpecialistNote, note_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Specialist note not found")
    for k, v in note.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/notes/{note_id}")
async def delete_specialist_note(note_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(SpecialistNote, note_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Specialist note not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True} 