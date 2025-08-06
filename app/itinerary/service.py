import asyncio
import uuid
from datetime import UTC, datetime
from typing import cast

from app.itinerary.error import INVALID_DESTINATION_ERROR
from app.itinerary.model import (ItineraryDocument, ItineraryDocumentStatus,
                                 TravelItinerary)
from app.itinerary.prompt import (PROMPT_SYSTEM_KEY, PROMPT_USER_KEY,
                                  get_prompt_create_itinerary)
from app.itinerary.repository import (create_itinerary_document,
                                      update_itinerary_document)
from app.itinerary.schema import CreateItineraryRequest
from app.openai import service
from app.openai.config import get_model
from app.openai.error import CallModelError


def _generate_create_itinerary_job_id() -> str:
    return str(uuid.uuid4())


async def _generate_travel_itinerary(
    *, itinerary_document: ItineraryDocument, request: CreateItineraryRequest
):
    prompt = get_prompt_create_itinerary(request=request)

    try:
        travel_itinerary = await service.parse_model_response(
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
        if travel_itinerary.itinerary is None:
            itinerary_document.error = INVALID_DESTINATION_ERROR
            itinerary_document.status = ItineraryDocumentStatus.FAILED
        else:
            itinerary_document.itinerary = travel_itinerary
            itinerary_document.status = ItineraryDocumentStatus.COMPLETED
    except CallModelError as e:
        itinerary_document.error = str(e)
        itinerary_document.status = ItineraryDocumentStatus.FAILED

    itinerary_document.completedAt = datetime.now(UTC)

    _ = update_itinerary_document(itinerary_document=itinerary_document)


async def create_itinerary(*, request: CreateItineraryRequest) -> str:
    job_id = _generate_create_itinerary_job_id()
    itinerary_document = ItineraryDocument(
        jobId=job_id,
        status=ItineraryDocumentStatus.PROCESSING,
        destination=request.destination,
        durationDays=request.durationDays,
        createdAt=datetime.now(UTC),
    )

    _ = create_itinerary_document(itinerary_document=itinerary_document)

    asyncio.create_task(
        _generate_travel_itinerary(
            itinerary_document=itinerary_document, request=request
        )
    )

    return job_id
