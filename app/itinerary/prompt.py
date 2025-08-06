from pathlib import Path

from yaml import safe_load

from app.itinerary.error import PromptKeyMissingError, PromptTypeError
from app.itinerary.schema import CreateItineraryRequest

_PROMPT_USER_KEY = "user"


def _get_prompt(key):
    base_path = Path(__file__).parent
    prompt_file_path = base_path / "prompt.yml"

    with open(prompt_file_path) as prompt_file:
        prompts = safe_load(prompt_file)

    if not key in prompts:
        raise PromptKeyMissingError(key)

    return prompts[key]


def get_prompt_create_itinerary(
    create_itinerary_request: CreateItineraryRequest,
) -> dict[str, str]:
    prompt = _get_prompt("create_itinerary")

    if not _PROMPT_USER_KEY in prompt:
        raise PromptTypeError()

    promt_user = prompt[_PROMPT_USER_KEY].format(
        destination=create_itinerary_request.destination,
        duration_days=create_itinerary_request.durationDays,
    )

    prompt[_PROMPT_USER_KEY] = promt_user

    return prompt
