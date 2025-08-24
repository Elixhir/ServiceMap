from service.domain.repositories.business import BusinessRepository
from service.domain.entities.business import Business

class GetNearbyBusinesses:
    def __init__(self, business_repo: BusinessRepository):
        self.business_repo = business_repo

    def execute(self, lat: float, long: float, radius: float = 500) -> list[Business]:

        if not (-90 <= lat <= 90) or not (-180 <= long <= 180):
            raise ValueError("Invalid coordinates")
        
        if radius <=0:
            raise ValueError("Radius must be greater than zero")
        
        business= self.business_repo.get_nearby_business(lat, long, radius)

        return business