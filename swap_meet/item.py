import uuid

class Item:
    # TODO understand how to apply id to inventory
    
    def __init__(self, id=None):
        if not id:
            id = uuid.uuid4().int
        self.id = id
    
    def get_category(self):
        return f'{self.__class__.__name__}'
    


