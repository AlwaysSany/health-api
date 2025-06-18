from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RoleResponse(RoleBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None

class PermissionCreate(PermissionBase):
    pass

class PermissionResponse(PermissionBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    class Config:
        from_attributes = True

class AuditLogBase(BaseModel):
    user_id: int
    action: str
    details: Optional[str] = None
    timestamp: Optional[datetime] = None

class AuditLogCreate(AuditLogBase):
    pass

class AuditLogResponse(AuditLogBase):
    id: int
    class Config:
        from_attributes = True 