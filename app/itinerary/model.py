from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class Activity(BaseModel):
    time: str
    description: str
    location: str


class DailyItinerary:
    day: int
    theme: str
    activities: List[Activity]


class TravelItinerary(BaseModel):
    itinerary: Optional[List[DailyItinerary]] = None


class ItineraryDocumentStatus(Enum):
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
