from typing import List
from sqlalchemy.orm import Session
from service.domain.entities.business import Business
from service.domain.repositories.business import BusinessRepository
from service.infrastructure.sqlalchemy_models.business import Business

class BusinessRepositoryImpl(BusinessRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_nearby(self, latitude: float, longitude: float, radius_km: float) -> List[Business]:
        # Earth radius in km
        R = 6371.0
        
        # Haversine formula
        query = self.db.query(Business).filter(
            f"""
            (acos(sin(radians({latitude})) * sin(radians(latitude)) + 
            cos(radians({latitude})) * cos(radians(latitude)) * 
            cos(radians(longitude) - radians({longitude}))) * {R}) <= {radius_km}
            """
        ).all()
        
        businesses = [
            Business(
                id=b.id,
                name=b.name,
                latitude=b.latitude,
                longitude=b.longitude,
                owner_id=b.owner_id
            )
            for b in query
        ]
        return businesses
