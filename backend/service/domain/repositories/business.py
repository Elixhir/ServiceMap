from abc import ABC
from service.domain.entities.business import Business

class BusinessRepository(ABC):

    def get_nearby_business(self, lat: float, lng: float, radius: float = 500) -> list[Business]:
        pass