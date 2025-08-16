from typing import Optional
from sqlalchemy.orm import Session
from service.domain.entities.user import User
from service.domain.repositories.user import UserRepository
from service.infrastructure.sqlalchemy_models.user import User as UserModel
from service.infrastructure.sqlalchemy_models.profile import Profile as ProfileModel
from service.infrastructure.sqlalchemy_models.subscription import Subscription as SubscriptionModel
from service.infrastructure.sqlalchemy_models.business import Business as BusinessModel

class UserRepositoryImpl(UserRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> Optional[User]:
        user = self.db.query(UserModel).filter(UserModel.email == email).first()
        if not user:
            return None
        return User(
            id=user.id,
            email=user.email,
            password_hash=user.password_hash,
            is_active=user.is_active,
            created_at=user.created_at
        )

    def create(self, user: User) -> User:
        return self._add_user_with_empty_relations(user)

    def add(self, user: User) -> User:
        return self._add_user_with_empty_relations(user)

    def _add_user_with_empty_relations(self, user: User) -> User:
        db_user = UserModel(
            email=user.email,
            password_hash=user.password_hash,
            is_active=user.is_active
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        profile = ProfileModel(user_id=db_user.id, full_name="", phone="", address="")
        subscription = SubscriptionModel(user_id=db_user.id, plan_name="", is_active=False)
        business = BusinessModel(owner_id=db_user.id, name="", description="", is_active=False, latitude=None, longitude=None)

        self.db.add_all([profile, subscription, business])
        self.db.commit()
        self.db.refresh(profile)
        self.db.refresh(subscription)
        self.db.refresh(business)

        return User(
            id=db_user.id,
            email=db_user.email,
            password_hash=db_user.password_hash,
            is_active=db_user.is_active,
            created_at=db_user.created_at
        )

    def exists_by_email(self, email: str) -> bool:
        return self.db.query(UserModel).filter(UserModel.email == email).first() is not None