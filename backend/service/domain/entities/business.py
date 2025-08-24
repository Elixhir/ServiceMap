from dataclasses import dataclass
from datetime import datetime

@dataclass
class Business():
    id: int
    name: str
    description: str
    is_active: bool
    latitude: float
    longitude: float
    created_at: datetime
    owner_id: int
