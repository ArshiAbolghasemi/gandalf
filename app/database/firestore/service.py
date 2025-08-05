from functools import lru_cache
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore import Client
from app.database.firestore.config import get_service_account_key


@lru_cache(maxsize=1)
def get_client() -> Client:
    if not firebase_admin._apps:
        cred = credentials.Certificate(get_service_account_key())
        firebase_admin.initialize_app(cred)

    return firestore.client()
