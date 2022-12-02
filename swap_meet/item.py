import uuid

class Item:
    def __init__(self, id= None) :
        if id is not None:
            self.id = id
        else:
            self.id = uuid.uuid4().int

    def get_category(self):
        return self.__class__.__name__

    def __str__(self) -> str:
        str_item = f"An object of type {self.get_category()} with id {self.id}"
        return str_item