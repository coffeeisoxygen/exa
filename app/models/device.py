from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from .base import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    serial = Column(String, unique=True, index=True)
    name = Column(String)
    model = Column(String)
    is_connected = Column(Boolean, default=False)
    last_connected = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Device {self.name} ({self.serial})>"
