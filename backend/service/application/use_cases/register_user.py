from domain.repositories.user import UserRepository
from domain.services.password_hasher import PasswordHasher
from ..dto import RegisterUserInput
from domain.entities.user import User
from domain.exceptions import UserAlreadyExistsError

class RegisterUser:
    def __init__(self, user_repo: UserRepository, hasher: PasswordHasher):
        self.user_repo = user_repo
        self.hasher = hasher

    def execute(self, data: RegisterUserInput) -> User:
        email = data.email.strip().lower()

        if self.user_repo.exists_by_email(email):
            raise UserAlreadyExistsError(f"User with email {email} already exists")
        
        user = User.create_with_password(email, data.password, self.hasher)

        saved_user = self.user_repo.add(user)
        return saved_user