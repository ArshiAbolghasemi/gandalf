from fastapi import APIRouter

from app.itinerary.api import router as itinerary_router


def get_router() -> APIRouter:
    router = APIRouter()

    router.include_router(router=itinerary_router)

    return router
