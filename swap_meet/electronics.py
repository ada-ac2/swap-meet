from .item import Item

class Electronics(Item):
    
    def __init__(self, id=None, condition=0, type="Unknown"):
        super().__init__(id, condition)
        self.type = type


    def __str__(self):
        electronics_str = (
            f"{super().__str__()}. " 
            f"This is a {self.type} device."
        )
        return electronics_str