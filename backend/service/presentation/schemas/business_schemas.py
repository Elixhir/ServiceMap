from pydantic import BaseModel
from typing import Optional

class BusinessBase(BaseModel):
    name: str

class Business(BusinessBase):
    id: int
    latitude: float
    longitude: float
    owner_id: int
    
    class Config:
        orm_mode = True

class BusinessNearby(Business):
    distance: float