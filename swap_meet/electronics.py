
#import parent class 
from swap_meet.item import Item
class Electronics(Item):

    def __init__(self, id=None, type=None, condition=None):
        super().__init__(id, condition)
        self.type = type if type is not None else "Unknown"
    
    def __str__(self):
        return (f"{super().__str__()}. This is a {self.type} device.")
