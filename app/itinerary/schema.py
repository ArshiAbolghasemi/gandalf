from typing import Optional
from pydantic import BaseModel, Field

from app.itinerary.model import ItineraryDocument, TravelItinerary


class CreateItineraryRequest(BaseModel):
    destination: str
    durationDays: int = Field(ge=1, le=10)


class CreateItineraryResponse(BaseModel):
    jobId: str

class CreateItineraryOpenAIResponse(BaseModel):
    itinerary: Optional[TravelItinerary] = None


class GetItineraryDocumentResponse(BaseModel):
    document: ItineraryDocument
