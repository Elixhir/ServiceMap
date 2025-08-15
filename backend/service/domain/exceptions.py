class DomainError(Exception):
    pass

class UserAlreadyExistsError(DomainError):
    pass

class InvalidCredentialsError(DomainError):
    pass

class InactiveUserError(DomainError):
    pass
