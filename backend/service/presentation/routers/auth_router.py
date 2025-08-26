from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from service.infrastructure.database.connection import get_db
from service.infrastructure.repositories.user_impl import UserRepositoryImpl
from service.application.use_cases.register_user import RegisterUser
from service.application.use_cases.login_user import LoginUser
from service.presentation.schemas.auth_schemas import RegisterRequest, LoginRequest
from service.application.dto import RegisterUserInput
from service.domain.services.bcrypt_hasher import BcryptPasswordHasher
from service.domain.exceptions import UserAlreadyExistsError
from sqlalchemy.exc import IntegrityError
from service.infrastructure.security.token_service import JWTTokenService
from service.domain.exceptions import InvalidCredentialsError

router = APIRouter()

@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    repo = UserRepositoryImpl(db)
    hasher = BcryptPasswordHasher() 
    use_case = RegisterUser(repo, hasher)
    request_data = RegisterUserInput(email=request.email, password=request.password)

    try:
        user = use_case.execute(request_data)
    except UserAlreadyExistsError:
        db.rollback()
        raise HTTPException(
            status_code=400, 
            detail=f"User with email {request_data.email} already exists"
        )
    except IntegrityError as e:
        db.rollback() 
        if 'ix_users_email' in str(e.orig):
            raise HTTPException(
                status_code=400, 
                detail=f"User with email {request_data.email} already exists"
            )
        else:
            raise HTTPException(status_code=500, detail="Database error")

    return {
        "user": {"id": user.id, "email": user.email}
    }

    
@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    repo = UserRepositoryImpl(db)
    hasher = BcryptPasswordHasher()
    token_service = JWTTokenService()
    use_case = LoginUser(repo, hasher, token_service)

    try:
        auth_output = use_case.execute(request)
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "id": auth_output.user_id,
        "email": auth_output.email,
        "access_token": auth_output.access_token,
        "token_type": "bearer"
    }

