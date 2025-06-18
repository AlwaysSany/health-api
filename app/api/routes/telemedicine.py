from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List
from app.api.dependencies.database import get_async_session
from app.api.dependencies.auth import get_current_active_user
from app.schemas.telemedicine import (
    VirtualVisitCreate, VirtualVisitResponse,
    ChatLogCreate, ChatLogResponse,
    VideoSessionCreate, VideoSessionResponse
)
from app.models.telemedicine import VirtualVisit, ChatLog, VideoSession
from app.models.user import User

router = APIRouter(prefix="/telemedicine", tags=["telemedicine"])

# VirtualVisit endpoints
@router.post("/visits/", response_model=VirtualVisitResponse)
async def create_virtual_visit(visit: VirtualVisitCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = VirtualVisit(**visit.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/visits/", response_model=List[VirtualVisitResponse])
async def list_virtual_visits(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(VirtualVisit))
    return result.scalars().all()

@router.get("/visits/{visit_id}", response_model=VirtualVisitResponse)
async def get_virtual_visit(visit_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(VirtualVisit, visit_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Virtual visit not found")
    return obj

@router.put("/visits/{visit_id}", response_model=VirtualVisitResponse)
async def update_virtual_visit(visit_id: int, visit: VirtualVisitCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(VirtualVisit, visit_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Virtual visit not found")
    for k, v in visit.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/visits/{visit_id}")
async def delete_virtual_visit(visit_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(VirtualVisit, visit_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Virtual visit not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# ChatLog endpoints
@router.post("/chats/", response_model=ChatLogResponse)
async def create_chat_log(chat: ChatLogCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = ChatLog(**chat.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/chats/", response_model=List[ChatLogResponse])
async def list_chat_logs(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(ChatLog))
    return result.scalars().all()

@router.get("/chats/{chat_id}", response_model=ChatLogResponse)
async def get_chat_log(chat_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(ChatLog, chat_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Chat log not found")
    return obj

@router.put("/chats/{chat_id}", response_model=ChatLogResponse)
async def update_chat_log(chat_id: int, chat: ChatLogCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(ChatLog, chat_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Chat log not found")
    for k, v in chat.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/chats/{chat_id}")
async def delete_chat_log(chat_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(ChatLog, chat_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Chat log not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True}

# VideoSession endpoints
@router.post("/videos/", response_model=VideoSessionResponse)
async def create_video_session(video: VideoSessionCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = VideoSession(**video.model_dump())
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.get("/videos/", response_model=List[VideoSessionResponse])
async def list_video_sessions(db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    result = await db.execute(select(VideoSession))
    return result.scalars().all()

@router.get("/videos/{video_id}", response_model=VideoSessionResponse)
async def get_video_session(video_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(VideoSession, video_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Video session not found")
    return obj

@router.put("/videos/{video_id}", response_model=VideoSessionResponse)
async def update_video_session(video_id: int, video: VideoSessionCreate, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(VideoSession, video_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Video session not found")
    for k, v in video.model_dump().items():
        setattr(obj, k, v)
    await db.commit()
    await db.refresh(obj)
    return obj

@router.delete("/videos/{video_id}")
async def delete_video_session(video_id: int, db: AsyncSession = Depends(get_async_session), current_user: User = Depends(get_current_active_user)):
    obj = await db.get(VideoSession, video_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Video session not found")
    await db.delete(obj)
    await db.commit()
    return {"ok": True} 