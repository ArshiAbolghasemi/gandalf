import asyncio
import uuid
from typing import cast

from app.itinerary.model import TravelItinerary
from app.itinerary.prompt import (
    PROMPT_SYSTEM_KEY,
    PROMPT_USER_KEY,
    get_prompt_create_itinerary,
)
from app.itinerary.repository import (
    create_itinerary_document,
    update_itinerary_document,
)
from app.itinerary.schema import CreateItineraryRequest
from app.openai import service
from app.openai.config import get_model


def _generate_create_itinerary_job_id() -> str:
    return str(uuid.uuid4())


async def _generate_travel_itinerary(
    *, destination: str, duration_days: int, job_id: str
):
    prompt = get_prompt_create_itinerary(
        destination=destination, duration_days=duration_days
    )

    travel_itinerary = service.parse_model_response(
        model=get_model(),
        input=[
            {
                "role": "system",
                "content": prompt[PROMPT_SYSTEM_KEY],
            },
            {
                "role": "user",
                "content": prompt[PROMPT_USER_KEY],
            },
        ],
        text_format=TravelItinerary,
    )

    travel_itinerary = cast(TravelItinerary, travel_itinerary)

    _ = update_itinerary_document(job_id=job_id, travel_itinerary=travel_itinerary)


async def create_itinerary(*, request: CreateItineraryRequest) -> str:
    job_id = _generate_create_itinerary_job_id()

    _ = create_itinerary_document(request=request, job_id=job_id)

    asyncio.create_task(
        _generate_travel_itinerary(
            destination=request.destination,
            duration_days=request.durationDays,
            job_id=job_id,
        )
    )

    return job_id
