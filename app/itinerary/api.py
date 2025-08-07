from fastapi import APIRouter, HTTPException, status

from app.database.firestore.error import DocumentNotFoundError
from app.itinerary import service
from app.itinerary.schema import (CreateItineraryRequest,
                                  CreateItineraryResponse,
                                  GetItineraryDocumentResponse)

router = APIRouter(prefix="/api/v1/itineraries", tags=["itinerary"])


@router.post(
    "", response_model=CreateItineraryResponse, status_code=status.HTTP_202_ACCEPTED
)
async def create_itinerary(request: CreateItineraryRequest):
    job_id = await service.create_itinerary(request=request)
    return CreateItineraryResponse(jobId=job_id)


@router.get("/{job_id}", response_model=GetItineraryDocumentResponse)
def get_itinerary(job_id: str):
    try:
        itinerary_document = service.get_itinerary(job_id=job_id)
        return GetItineraryDocumentResponse(document=itinerary_document)
    except DocumentNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
