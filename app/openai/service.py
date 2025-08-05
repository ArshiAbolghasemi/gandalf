from functools import lru_cache

from openai import OpenAI

from app.openai.config import get_api_key, get_base_url, get_timeout


@lru_cache(maxsize=1)
def get_client():
    return OpenAI(api_key=get_api_key(), base_url=get_base_url(), timeout=get_timeout())
