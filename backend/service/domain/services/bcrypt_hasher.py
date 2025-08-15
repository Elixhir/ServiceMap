from service.domain.services.password_hasher import PasswordHasher
import bcrypt

class BcryptPasswordHasher(PasswordHasher):
    def hash(self, raw_password: str) -> str:
        return bcrypt.hashpw(raw_password.encode(), bcrypt.gensalt()).decode()

    def verify(self, raw_password: str, password_hash: str) -> bool:
        return bcrypt.checkpw(raw_password.encode(), password_hash.encode())
