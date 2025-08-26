from datetime import datetime, timedelta
import jwt
from service.domain.services.token import Token
from service.domain.entities.user import User
import os
from dotenv import load_dotenv
load_dotenv()

JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class JWTTokenService(Token):
    def create_access_token(self, user: User) -> str:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {
            "sub": str(user.id),
            "email": user.email,
            "exp": expire
        }
        return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)

    def decode(self, token: str):
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
