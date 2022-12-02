import uuid
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, fabric = "Unknown", id = None, condition = 0):
        super().__init__()
        self.id = id if id is not None else uuid.uuid1().int
        self.fabric = fabric
        self.condition = condition

    def get_category(self):
        return "Clothing"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."