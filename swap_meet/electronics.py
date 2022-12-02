from .item import Item

class Electronics(Item):
    def __init__(self, id = None, condition = 0, type = "Unknown"):
        super().__init__(id, condition)
        self.type = type
    
    def __str__(self):
        return f"{super().__str__()}. This is a {self.type} device."