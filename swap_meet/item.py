import uuid
class Item:
    def __init__(self, id=None):
        unique_identifier = uuid.uuid4()
        self.id = id if id else unique_identifier.int
    def get_category(self):
        return self.__class__.__name__
    
