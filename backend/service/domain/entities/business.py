from dataclasses import dataclass
from datetime import datetime

@dataclass
class Business():
    id: int
    name: str
    description: str
    latitude: float
    longitude: float
    owner_id: int
    category: str
    address: str
    phone: str
    is_active: bool = True
    created_at: datetime = datetime.utcnow()
