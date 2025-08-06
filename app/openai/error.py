class ConfigMissingError(Exception):

    def __init__(self, missing_key: str):
        self._missing_key = missing_key
        super().__init__(missing_key)

    def __str__(self) -> str:
        return f"Openapi {self._missing_key} is missed!"


class CallModelError(Exception):

    def __init__(self, error: BaseException) -> None:
        self._error = error
        super().__init__(error)

    def __str__(self) -> str:
        return f"Failed to call Model {str(self._error)}"
