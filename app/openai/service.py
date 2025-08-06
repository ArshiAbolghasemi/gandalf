import asyncio
import random
from functools import lru_cache

from openai import OpenAI

from app.openai.config import get_api_key, get_base_url, get_timeout
from app.openai.error import CallModelError


@lru_cache(maxsize=1)
def get_client():
    return OpenAI(api_key=get_api_key(), base_url=get_base_url(), timeout=get_timeout())


_MAX_RETRIES = 5
_INITIAL_BACKOFF_SECONDS = 1


async def parse_model_response(*, model: str, input, text_format):
    client = get_client()

    for attempt in range(_MAX_RETRIES):
        try:
            response = client.responses.parse(
                model=model, input=input, text_format=text_format
            )
            return response.output_parsed
        except BaseException as e:
            if attempt + 1 == _MAX_RETRIES:
                raise CallModelError(e)

            back_off = _INITIAL_BACKOFF_SECONDS * (2 ** (attempt))
            jitter = random.uniform(0, 1)
            await asyncio.sleep(back_off + jitter)
