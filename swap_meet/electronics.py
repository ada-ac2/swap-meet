# Wave 5
import uuid
from swap_meet.item import Item
class Electronics(Item):
    def __init__(self,id = None,category = "" ,condition = 0 ,type = "Unknown"):
        super().__init__(id,category,condition)
        self.type = type
        
    def __str__(self):
        item_message = super().__str__()
        return f"{item_message}. This is a {self.type} device."
    