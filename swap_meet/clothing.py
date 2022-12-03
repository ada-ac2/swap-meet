from swap_meet.item import Item

class Clothing (Item):
    def __init__(self, id=None, fabric = "Unknown"):
        super().__init__(id)
        self.fabric = fabric

    def __str__(self) -> str:
        cloth_str = super().__str__() + f". It is made from {self.fabric} fabric."
        return cloth_str