class ConfigMissingError(Exception):

    def __init__(self, missing_key: str):
        self._missing_key = missing_key
        super().__init__(missing_key)

    def __str__(self) -> str:
        return f"Firestore {self._missing_key} is missed!"


class DocumentNotFoundError(Exception):

    def __init__(self, doc_id):
        self._doc_id = doc_id
        super().__init__(doc_id)

    def __str__(self) -> str:
        return f"firestore document {self._doc_id} is not found!"
