from pydantic import BaseModel
from typing import Optional

class BusinessBase(BaseModel):
    name: str
    category: Optional[str] = None
    description: Optional[str] = None
    latitude: float
    longitude: float
    address: Optional[str] = None
    phone: Optional[str] = None

class Business(BusinessBase):
    id: int
    latitude: float
    longitude: float
    owner_id: int
    
    class Config:
        from_attributes = True

class BusinessNearby(Business):
    distance: float

class BusinessCreate(BusinessBase):
    pass

class BusinessOut(BusinessBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
