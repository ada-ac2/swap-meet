import uuid
from swap_meet.item import Item
class Clothing(Item):

    def __init__(self, id=None, fabric=None) :
        super().__init__(id)
        if fabric:
            self.fabric = fabric
            self.fabric = fabric
        else:
            self.fabric = "Unknown"
    #是否使用super()?
    #def get_category(self):
        #super().get_category()
    def get_category(self):
        return f"{self.__class__.__name__}"
        #return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."
    def def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."
