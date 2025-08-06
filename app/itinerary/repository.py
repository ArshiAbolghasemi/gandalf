from google.cloud.firestore import DocumentReference

from app.database.firestore.service import get_client
from app.itinerary.model import ItineraryDocument

_ITITENERARY_COLLECTION = "itinerary"


def _get_itinerary_document_by_job_id(*, job_id: str) -> DocumentReference:
    db = get_client()
    return db.collection(_ITITENERARY_COLLECTION).document(job_id)


def create_itinerary_document(
    *, itinerary_document: ItineraryDocument
) -> DocumentReference:
    doc = _get_itinerary_document_by_job_id(job_id=itinerary_document.jobId)
    doc.set(itinerary_document.model_dump())

    return doc


def update_itinerary_document(
    *, itinerary_document: ItineraryDocument
) -> DocumentReference:
    doc = _get_itinerary_document_by_job_id(job_id=itinerary_document.jobId)
    doc.set(itinerary_document.model_dump(), merge=True)

    return doc
