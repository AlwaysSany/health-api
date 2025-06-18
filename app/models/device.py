from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base import Base

class WearableDevice(Base):
    __tablename__ = "wearable_devices"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    device_type = Column(String(100), nullable=False)
    manufacturer = Column(String(100))
    serial_number = Column(String(100), unique=True)
    registered_at = Column(DateTime(timezone=True), server_default=func.now())

class DeviceData(Base):
    __tablename__ = "device_data"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("wearable_devices.id"), nullable=False)
    data_type = Column(String(100), nullable=False)
    value = Column(Float)
    unit = Column(String(20))
    recorded_at = Column(DateTime(timezone=True), nullable=False)

class RemoteMonitoringLog(Base):
    __tablename__ = "remote_monitoring_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    device_id = Column(Integer, ForeignKey("wearable_devices.id"), nullable=False)
    log = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 