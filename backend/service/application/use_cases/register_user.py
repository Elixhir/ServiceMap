from service.domain.repositories.user import UserRepository
from service.domain.services.password_hasher import PasswordHasher
from ..dto import RegisterUserInput
from service.domain.entities.user import User
from service.domain.exceptions import UserAlreadyExistsError

class RegisterUser:
    def __init__(self, user_repo: UserRepository, hasher: PasswordHasher):
        self.user_repo = user_repo
        self.hasher = hasher

    def execute(self, data: RegisterUserInput) -> User:
        email = data.email.strip().lower()
        user = User.create_with_password(email, data.password, self.hasher)
        saved_user = self.user_repo.add(user)
        return saved_user