from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class DayTime(str, Enum):
    MORNING = "Morning"
    AFTERNOON = "Afternoon"
    EVENING = "Evening"
    NIGHT = "Night"


class Activity(BaseModel):
    time: DayTime
    description: str
    location: str


class DailyItinerary(BaseModel):
    day: int
    theme: str
    activities: List[Activity]


TravelItinerary = List[DailyItinerary]


class ItineraryDocumentStatus(str, Enum):
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class ItineraryDocument(BaseModel):
    jobId: str
    status: ItineraryDocumentStatus
    destination: str
    durationDays: int
    createdAt: datetime
    completedAt: Optional[datetime] = None
    itinerary: Optional[TravelItinerary] = None
    error: Optional[str] = None
