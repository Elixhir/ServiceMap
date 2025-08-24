from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from service.domain.exceptions import InactiveUserError

@dataclass
class User:
    id: int
    email: str
    password_hash: str
    is_active: bool = True
    created_at: Optional[datetime] = None

    def ensure_active(self):
        if not self.is_active:
            raise InactiveUserError("User is inactive")
        
    def verify_password(self, raw_password: str, hasher: "PasswordHasher") -> bool: # type: ignore
        return hasher.verify(raw_password, self.password_hash)
    
    @classmethod
    def create_with_password(cls, email:str, raw_password: str, hasher: "PasswordHasher") -> User: # type: ignore
        normalized = email.strip().lower()
        hashed = hasher.hash(raw_password)
        return cls(id=None, email=normalized, password_hash=hashed, is_active=True)