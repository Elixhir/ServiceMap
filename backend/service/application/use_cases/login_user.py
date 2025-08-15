from domain.repositories.user import UserRepository
from domain.services.password_hasher import PasswordHasher
from domain.services.token import Token
from domain.exceptions import InvalidCredentialsError
from application.dto import LoginUserInput, AuthOutput


class LoginUser:
    def __init__(self, user_repo: UserRepository, hasher: PasswordHasher, token_service: Token):
        self.user_repo = user_repo
        self.hasher = hasher
        self.token_service = token_service

    def execute(self, data: LoginUserInput) -> AuthOutput:
        email = data.email.strip().lower()

        user = self.user_repo.get_by_email(email)
        if not user:
            raise InvalidCredentialsError("Invalid email or password")

        if not self.hasher.verify(data.password, user.password_hash):
            raise InvalidCredentialsError("Invalid email or password")

        user.ensure_active()

        token = self.token_service.create_access_token(subject=str(user.id))
        return AuthOutput(access_token=token)
