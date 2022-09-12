import uuid

class Item:
    def __init__(self, id=None) -> None:            
        self.id = id if id else uuid.uuid4().int

    def get_category(self):
        return type(self).__name__

    def __str__(self) -> str:
        return f"An object of type {self.get_category()} with id {self.id}"