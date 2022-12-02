import uuid

class Item:
    def __init__(self, id=None):
        self.id = uuid.uuid1().int if not id else id

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}"
