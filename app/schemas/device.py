from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class WearableDeviceBase(BaseModel):
    user_id: int
    device_type: str
    manufacturer: Optional[str] = None
    serial_number: Optional[str] = None
    registered_at: Optional[datetime] = None

class WearableDeviceCreate(WearableDeviceBase):
    pass

class WearableDeviceResponse(WearableDeviceBase):
    id: int
    class Config:
        from_attributes = True

class DeviceDataBase(BaseModel):
    device_id: int
    data_type: str
    value: Optional[float] = None
    unit: Optional[str] = None
    recorded_at: datetime

class DeviceDataCreate(DeviceDataBase):
    pass

class DeviceDataResponse(DeviceDataBase):
    id: int
    class Config:
        from_attributes = True

class RemoteMonitoringLogBase(BaseModel):
    user_id: int
    device_id: int
    log: str
    created_at: Optional[datetime] = None

class RemoteMonitoringLogCreate(RemoteMonitoringLogBase):
    pass

class RemoteMonitoringLogResponse(RemoteMonitoringLogBase):
    id: int
    class Config:
        from_attributes = True 