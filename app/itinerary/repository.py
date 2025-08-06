from firebase_admin.firestore import firestore
from google.cloud.firestore import DocumentReference

from app.database.firestore.service import get_client
from app.itinerary.model import ItineraryDocumentStatus, TravelItinerary
from app.itinerary.schema import CreateItineraryRequest

_ITITENERARY_COLLECTION = "itinerary"


def create_itinerary_document(
    *, request: CreateItineraryRequest, job_id: str
) -> DocumentReference:
    db = get_client()
    doc = db.collection(_ITITENERARY_COLLECTION).document(job_id)
    doc.set(
        {
            "status": ItineraryDocumentStatus.PROCESSING.value,
            "destination": request.destination,
            "durationDays": request.durationDays,
            "createdAt": firestore.SERVER_TIMESTAMP,
            "completedAt": None,
            "itinerary": None,
            "error": None,
        }
    )

    return doc


def update_itinerary_document(
    *, job_id: str, travel_itinerary: TravelItinerary
) -> DocumentReference:
    doc = get_client(_ITITENERARY_COLLECTION).document(job_id)

    data = {}
    if travel_itinerary.itinerary is None:
        data["status"] = ItineraryDocumentStatus.FAILED.value
    else:
        data["itinerary"] = travel_itinerary.itinerary
        data["status"] = ItineraryDocumentStatus.COMPLETED.value

    doc.set(data)

    return doc
