from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=None, fabric=None):
        super().__init__(id, "Clothing", condition)
        self.fabric = fabric if fabric is not None else "Unknown"

    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."

    def get_category(self):
        return self.category