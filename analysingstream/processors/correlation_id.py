import uuid


class CorrelationId:
    id: str

    def __init__(self, title):
        self.id = f"{title} ({uuid.uuid4()})"

    def __str__(self):
        return self.id

    def continue_with(self, title):
        return CorrelationId(f"{self.id}-{title}")
