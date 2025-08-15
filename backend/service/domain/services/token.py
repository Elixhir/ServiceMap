from abc import ABC, abstractmethod
from typing import Optional, Mapping
from datetime import timedelta

class Token(ABC):
    
    @abstractmethod
    def create_access_token(
        self, 
        subject: str, 
        claims: Optional[Mapping[str, str]] = None,
        expires_delta: Optional[timedelta] = None
    ) -> str:
        pass

    @abstractmethod
    def decode(self, token: str) -> Mapping[str, str]:
        pass