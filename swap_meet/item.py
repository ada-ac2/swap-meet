import uuid

class Item:
    def __init__(self, id=None):
        self.id = id if id else uuid.uuid4().int

    
    def __str__(self):
        return self.__class__.__name__
    
    def get_category(self):
        return self.__str__()
