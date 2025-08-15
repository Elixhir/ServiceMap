from abc import ABC, abstractmethod
from typing import Optional
from service.domain.entities.user import User

class UserRepository(ABC):

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass

    @abstractmethod
    def add(self, user: User) -> User:
        pass

    @abstractmethod
    def exists_by_email(self, email: str) -> bool:
        pass