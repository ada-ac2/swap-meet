# Wave 5
import uuid
from swap_meet.item import Item
class Decor(Item):
    def __init__(self,id = None,category = "" ,condition = 0,width = 0,length = 0 ):
        super().__init__(id,category,condition)
        self.width = width
        self.length = length
    
    def __str__(self):
        item_message = super().__str__()
        return f"{item_message}. It takes up a {self.width} by {self.length} sized space."