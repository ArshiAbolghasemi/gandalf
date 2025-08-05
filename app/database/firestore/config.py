import os
from typing import Any, Dict

from app.database.firestore.error import ConfigMissingError


def _get_env_var(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ConfigMissingError(key)
    return value


def _get_type() -> str:
    return _get_env_var("FIREBASE_TYPE")


def _get_project_id() -> str:
    return _get_env_var("FIREBASE_PROJECT_ID")


def _get_private_key_id() -> str:
    return _get_env_var("FIREBASE_PRIVATE_KEY_ID")


def _get_private_key() -> str:
    return _get_env_var("FIREBASE_PRIVATE_KEY")


def _get_client_email() -> str:
    return _get_env_var("FIREBASE_CLIENT_EMAIL")


def _get_client_id() -> str:
    return _get_env_var("FIREBASE_CLIENT_ID")


def _get_auth_uri() -> str:
    return _get_env_var("FIREBASE_AUTH_URI")


def _get_token_uri() -> str:
    return _get_env_var("FIREBASE_TOKEN_URI")


def _get_auth_provider_x509_cert_url() -> str:
    return _get_env_var("FIREBASE_AUTH_PROVIDER_X509_CERT_URL")


def _get_client_x509_cert_url() -> str:
    return _get_env_var("FIREBASE_CLIENT_X509_CERT_URL")


def _get_universe_domain() -> str:
    return _get_env_var("FIREBASE_UNIVERSE_DOMAIN")


def get_service_account_key() -> Dict[str, Any]:
    return {
        "type": _get_type(),
        "project_id": _get_project_id(),
        "private_key_id": _get_private_key_id(),
        "private_key": _get_private_key(),
        "client_email": _get_client_email(),
        "client_id": _get_client_id(),
        "auth_uri": _get_auth_uri(),
        "token_uri": _get_token_uri(),
        "auth_provider_x509_cert_url": _get_auth_provider_x509_cert_url(),
        "client_x509_cert_url": _get_client_x509_cert_url(),
        "universe_domain": _get_universe_domain(),
    }
