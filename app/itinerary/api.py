from fastapi import APIRouter, status

from app.itinerary import service
from app.itinerary.schema import (CreateItineraryRequest,
                                  CreateItineraryResponse)

router = APIRouter(prefix="/api/v1/itinerary", tags=["itinerary"])


@router.post(
    "", response_model=CreateItineraryResponse, status_code=status.HTTP_202_ACCEPTED
)
async def create_itinerary(request: CreateItineraryRequest):
    job_id = await service.create_itinerary(request=request)
    return CreateItineraryResponse(jobId=job_id)
