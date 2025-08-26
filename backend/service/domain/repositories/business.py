from abc import ABC, abstractmethod
from service.domain.entities.business import Business

class BusinessRepository(ABC):

    @abstractmethod
    def get_nearby_business(self, lat: float, lng: float, radius: float = 500) -> list[Business]:
        pass

    @abstractmethod
    def create_business(self, business: Business) -> Business:
        pass