class PromptTypeError(TypeError):
    def __str__(self) -> str:
        return "Invalid itinerary package prompt file format"


class PromptKeyMissingError(KeyError):
    def __init__(self, key):
        self._key = key
        super().__init__(key)

    def __str__(self) -> str:
        return f"Prompt {self._key} is not existed in itinerary package"

INVALID_DESTINATION_ERROR = "Destination is invalid!"
