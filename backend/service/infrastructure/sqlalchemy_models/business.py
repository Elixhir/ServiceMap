from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, func, Float
from sqlalchemy.orm import relationship
from service.infrastructure.database.connection import Base

class Business(Base):
    __tablename__ = "businesses"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    is_active = Column(Boolean, default=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship(
        "User",
        back_populates="business",
    )

