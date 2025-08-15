from __future__ import annotations
from abc import ABC, abstractmethod

class PasswordHasher(ABC):

    @abstractmethod
    def hash(self, raw_password: str) -> str:
        pass

    @abstractmethod
    def verify(self, raw_password: str, password_hash: str) -> str:
        pass