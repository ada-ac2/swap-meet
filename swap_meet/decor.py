import uuid
from swap_meet.item import Item
class Decor(Item):

    def __init__(self, id=None, width=None, length =None) :
        super().__init__(id)
        if width or length:
            self.width = width
            self.length = length
        else:
            self.width = 0
            self.length = 0
    #是否使用super()?
    #def get_category(self):
        #super().get_category()
    def get_category(self):
        return f"{self.__class__.__name__}"
        #return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It takes up a {self.width} by {self.length} sized space."