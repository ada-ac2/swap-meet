import uuid

class Item:
    def __init__(self, id=None):
        if id == None:
            self.id = uuid.uuid1().int
        else:
            self.id=id

    def get_category(self):
        return type(self).__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}"