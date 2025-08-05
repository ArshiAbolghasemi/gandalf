class ConfigMissingError(Exception):

    def __init__(self, missing_key):
        self._missing_key = missing_key
        super().__init__(missing_key)

    def __str__(self) -> str:
        return f"Openapi {self._missing_key} is missed!"
