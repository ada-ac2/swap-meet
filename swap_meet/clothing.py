import uuid
from swap_meet.item import Item
class Clothing(Item):

    def __init__(self, id=None, condition=None, fabric=None) :
        super().__init__(id, condition)
        if fabric:
            if type(fabric) is not str:
                raise TypeError("Type fabric is string")
            self.fabric = fabric
            
        else:
            self.fabric = "Unknown"
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It is made from {self.fabric} fabric."
    