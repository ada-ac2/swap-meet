import uuid
from swap_meet.item import Item
class Electronics(Item):

    def __init__(self, id=None, condition=None, type=None) :
        
        super().__init__(id, condition)
        if type:
            self.type = type
        else:
            self.type = "Unknown"
   
    
    def __str__(self):   
        return f"An object of type {self.get_category()} with id {self.id}. This is a {self.type} device."
