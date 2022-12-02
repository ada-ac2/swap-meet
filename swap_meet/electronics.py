import uuid
from .item import Item


class Electronics(Item):
    
    def __init__(self, id=None, type="Unknown", condition=0):
        super().__init__(id, condition)
        self.type = type
    
    def __str__(self):
        """
        return a message about the electronics instance
        """
        stringified = super().__str__() + f". This is a {self.type} device."
        return stringified
    

