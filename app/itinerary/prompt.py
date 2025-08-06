from pathlib import Path

from yaml import safe_load

from app.itinerary.error import PromptKeyMissingError, PromptTypeError

PROMPT_USER_KEY = "user"
PROMPT_SYSTEM_KEY = "system"


def _get_prompt(key):
    base_path = Path(__file__).parent
    prompt_file_path = base_path / "prompt.yml"

    with open(prompt_file_path) as prompt_file:
        prompts = safe_load(prompt_file)

    if not key in prompts:
        raise PromptKeyMissingError(key)

    return prompts[key]


def get_prompt_create_itinerary(
    *, destination: str, duration_days: int
) -> dict[str, str]:
    prompt = _get_prompt("create_itinerary")

    if not PROMPT_USER_KEY in prompt or not PROMPT_SYSTEM_KEY in prompt:
        raise PromptTypeError()

    promt_user = prompt[PROMPT_USER_KEY].format(
        destination=destination,
        duration_days=duration_days,
    )

    prompt[PROMPT_USER_KEY] = promt_user

    return prompt
