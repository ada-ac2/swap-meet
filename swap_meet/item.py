import uuid

class Item:
    def __init__(self, id=None):
        self.id = id if id else uuid.uuid4().int
    
    def get_category(self):
        return f"{self.class_name}" # string holding name of the class?
    
    #### wave 3