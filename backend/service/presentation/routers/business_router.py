from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from service.domain.entities.business import Business
from service.application.use_cases.get_nearby_businesses import GetNearbyBusinesses
from service.application.use_cases.register_business import RegisterBusiness
from service.infrastructure.database.connection import get_db
from service.presentation.schemas.business_schemas import Business as BusinessSchema
from service.presentation.schemas.business_schemas import BusinessNearby
from service.presentation.schemas.business_schemas import BusinessCreate, BusinessOut
from service.infrastructure.repositories.business_impl import BusinessRepositoryImpl
from service.utils.get_current_user import get_current_user

router = APIRouter()

@router.get("/nearby", response_model=List[BusinessNearby])
def get_nearby_businesses(
    latitude: float = Query(..., description="Client's latitude"),
    longitude: float = Query(..., description="Client's longitude"),
    radius: float = Query(5.0, description="Search radius in kilometers"),
    db: Session = Depends(get_db)
):
    try:
        business_repository = BusinessRepositoryImpl(db)
        
        get_nearby_use_case = GetNearbyBusinesses(business_repository)
        
        businesses = get_nearby_use_case.execute(latitude, longitude, radius)
        
        response = []
        for business in businesses:
            response.append(BusinessNearby(
                id=business.id,
                name=business.name,
                latitude=business.latitude,
                longitude=business.longitude,
                owner_id=business.owner_id,
                distance=0.0 
            ))
        return response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
    
@router.post("/register", response_model=BusinessOut)
def create_business(
    request: BusinessCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user),
):
    repo = BusinessRepositoryImpl(db)
    use_case = RegisterBusiness(repo)

    business = Business(
        id=None,
        owner_id=current_user.id,
        name=request.name,
        category=request.category,
        description=request.description,
        latitude=request.latitude,
        longitude=request.longitude,
        address=request.address,
        phone=request.phone,
    )

    try:
        result = use_case.execute(business, has_active_subscription=current_user.has_active_subscription)
        return result
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
