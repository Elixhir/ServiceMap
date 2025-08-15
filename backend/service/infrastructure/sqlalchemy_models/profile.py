from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from service.infrastructure.database.connection import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    full_name = Column(String)
    phone = Column(String)
    address = Column(String)

    user = relationship(
        "User",
        back_populates="profile",
    )

