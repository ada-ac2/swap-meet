import uuid
from .item import Item


class Clothing(Item):

    def __init__(self, id=None, fabric="Unknown", condition=0):
        super().__init__(id, condition)
        self.fabric = fabric
    
    def __str__(self):
        """
        return a message about the clothing instance
        """
        stringified = super().__str__() + f". It is made from {self.fabric} fabric."
        return stringified

