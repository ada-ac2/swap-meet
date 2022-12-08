import uuid
class Clothing:
    def __init__(self, id=None, fabric="Unknown"):
        if id is None:
            self.id =uuid.uuid4().int
        else:
            self.id = id
        self.fabric = fabric
    
    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."