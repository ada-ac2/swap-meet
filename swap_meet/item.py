import uuid

class Item:
    def __init__(self, id=None):
        self.id = id if id else uuid.uuid4().int
    
    def __str__(self):
        # override Item stringify method and instead return this string when str(self) called        
        return f'An object of type Item with id {self.id}'
    
    def get_category(self):
        return type(self).__name__