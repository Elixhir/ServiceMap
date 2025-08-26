from typing import List
from sqlalchemy.orm import Session
from service.domain.entities.business import Business
from service.domain.repositories.business import BusinessRepository
from service.infrastructure.sqlalchemy_models.business import Business as BusinessModel
import math

class BusinessRepositoryImpl(BusinessRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_nearby_business(self, lat: float, lng: float, radius: float = 500) -> List[Business]:
        EARTH_RADIUS = 6371000  # metros
        lat_r = math.radians(lat)
        lng_r = math.radians(lng)

        businesses = self.db.query(BusinessModel).all()

        nearby = []
        for b in businesses:
            d = self._haversine(lng, lat, b.longitude, b.latitude)
            if d <= radius:
                nearby.append(
                    Business(
                        id=b.id,
                        user_id=b.user_id,
                        name=b.name,
                        category=b.category,
                        description=b.description,
                        latitude=b.latitude,
                        longitude=b.longitude,
                        address=b.address,
                        phone=b.phone,
                        created_at=b.created_at,
                    )
                )
        return nearby

    def _haversine(self, lon1, lat1, lon2, lat2):
        # Fórmula Haversine para calcular distancia en metros
        R = 6371000  # radio Tierra en metros
        phi1, phi2 = math.radians(lat1), math.radians(lat2)
        dphi = math.radians(lat2 - lat1)
        dlambda = math.radians(lon2 - lon1)

        a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
        return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    def create_business(self, business: Business) -> Business:
        db_business = BusinessModel(
            owner_id=business.owner_id,
            name=business.name,
            category=business.category,
            description=business.description,
            latitude=business.latitude,
            longitude=business.longitude,
            address=business.address,
            phone=business.phone,
        )
        self.db.add(db_business)
        self.db.commit()
        self.db.refresh(db_business)

        return Business(
            id=db_business.id,
            owner_id=db_business.owner_id,
            name=db_business.name,
            category=db_business.category,
            description=db_business.description,
            latitude=db_business.latitude,
            longitude=db_business.longitude,
            address=db_business.address,
            phone=db_business.phone,
            created_at=db_business.created_at,
        )