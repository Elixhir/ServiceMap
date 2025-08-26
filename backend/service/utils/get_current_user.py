from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from service.infrastructure.security.token_service import JWTTokenService
from service.presentation.schemas.auth_schemas import CurrentUser

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
token_service = JWTTokenService()

def get_current_user(token: str = Depends(oauth2_scheme)) -> CurrentUser:
    try:
        payload = token_service.decode(token)
        return CurrentUser(
            id=int(payload.get("sub")),
            email=payload.get("email"),
            has_active_subscription=True
        )
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
