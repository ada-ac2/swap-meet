from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric

    def __str__(self):
        return f"{super().__str__()}. It is made from {self.fabric} fabric."
    
    def is_similar(self, other_item):
        return other_item.fabric == self.fabric