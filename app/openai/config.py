import os
from dotenv import load_dotenv

from app.openai.error import ConfigMissingError

load_dotenv()


def _get_env_variable(key: str) -> str:
    value = os.getenv(key)
    if value is None:
        raise ConfigMissingError(key)
    return value


def get_api_key() -> str:
    return _get_env_variable("OPENAI_API_KEY")


def get_base_url() -> str:
    return _get_env_variable("OPENAI_BASE_URL")


def get_model() -> str:
    return _get_env_variable("OPENAI_MODEL")


def get_timeout() -> int:
    return int(_get_env_variable("OPENAI_TIMEOUT"))
