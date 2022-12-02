import uuid
from swap_meet.item import Item
class Decor(Item):

    def __init__(self, id=None, condition=None, width=None, length =None) :
        super().__init__(id, condition)
        if width or length:
            self.width = width
            self.length = length
        else:
            self.width = 0
            self.length = 0
    
    
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It takes up a {self.width} by {self.length} sized space."

    