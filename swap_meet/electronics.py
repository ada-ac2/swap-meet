import uuid
from swap_meet.item import Item
class Electronics(Item):

    def __init__(self, id=None, condition=None, type=None) :
        
        super().__init__(id, condition)
        if type:
            self.type = type
        else:
            self.type = "Unknown"
    #是否使用super()?
    #def get_category(self):
        #super().get_category()
    def get_category(self):
        return f"{self.__class__.__name__}"
        #return f"An object of type {self.__class__.__name__} with id {self.id}. It is made from {self.fabric} fabric."
    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. This is a {self.type} device."
    def condition_description(self):
        Item.condition_description()