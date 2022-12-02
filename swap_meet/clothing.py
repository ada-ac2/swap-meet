from .item import Item
class Clothing(Item):
    def __init__(self, id=None, fabric = "Unknown"):
        super().__init__(id)
        self.fabric = fabric

    def __repr__(self):
        return f"{super().__repr__()}. It is made from {self.fabric} fabric."