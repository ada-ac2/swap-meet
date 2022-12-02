import uuid

class Item:
    def __init__(self, id = None):
        #maybe check if id already exists so that there won't be duplicates??
        self. id = uuid.uuid4().int if id is None else id

    def get_category(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"An object of type {self.get_category()} with id {self.id}"

    