import uuid

class Item:
    def __init__(self, id=None):
        self.id = id if id else uuid.uuid4().int
        

    
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}"
    
    def get_category(self):
        return self.__class__.__name__
