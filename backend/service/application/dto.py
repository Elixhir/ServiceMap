from dataclasses import dataclass

@dataclass
class RegisterUserInput:
    email: str
    password: str

@dataclass
class LoginUserInput:
    email: str
    password: str

@dataclass
class AuthOutput:
    access_token: str
    user_id: int
    email: str

