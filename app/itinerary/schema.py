from pydantic import BaseModel, Field


class CreateItineraryRequest(BaseModel):
    destination: str
    durationDays: int = Field(ge=1, le=10)


class CreateItineraryResponse(BaseModel):
    jobId: str
