from service.domain.repositories.business import BusinessRepository
from service.domain.entities.business import Business

class RegisterBusiness:
    def __init__(self, business_repo = BusinessRepository):
        self.business_repo = business_repo

    def execute(self, business: Business, has_active_subscription: bool) -> Business:

        if not has_active_subscription:
            raise PermissionError("Do you need a subscription to register")

        return self.business_repo.create_business(business)