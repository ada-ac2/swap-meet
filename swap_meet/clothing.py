from .item import Item

class Clothing(Item):
    
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric


    def __str__(self):
        clothing_str = (
            f"{super().__str__()}. " 
            f"It is made from {self.fabric} fabric."
        )
        return clothing_str

        