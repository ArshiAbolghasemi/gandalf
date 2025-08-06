from pydantic import BaseModel, Field

from app.itinerary.model import ItineraryDocument


class CreateItineraryRequest(BaseModel):
    destination: str
    durationDays: int = Field(ge=1, le=10)


class CreateItineraryResponse(BaseModel):
    jobId: str


class GetItineraryDocumentResponse(BaseModel):
    document: ItineraryDocument
