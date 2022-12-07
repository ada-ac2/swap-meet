# Wave 5
import uuid
from swap_meet.item import Item
class Clothing(Item):
    def __init__(self,id= None,category = "" ,condition = 0 ,fabric = "Unknown" ):
        super().__init__(id,category,condition)
        self.fabric = fabric
    
    def __str__(self):
        item_message = super().__str__()
        return f"{item_message}. It is made from {self.fabric} fabric."