import uuid

class Item:
    
    def __init__(self, id = None):
        self.id = id if id is not None else uuid.uuid1().int

    def get_category(self):
        return 'Item'