from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from service.domain.entities.business import Business
from service.application.use_cases.get_nearby_businesses import GetNearbyBusinesses
from service.infrastructure.repositories.business_impl import BusinessRepositoryImpl
from service.infrastructure.database.connection import get_db
from service.presentation.schemas.business_schemas import Business as BusinessSchema
from service.presentation.schemas.business_schemas import BusinessNearby

router = APIRouter()

@router.get("/businesses/nearby", response_model=List[BusinessNearby])
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