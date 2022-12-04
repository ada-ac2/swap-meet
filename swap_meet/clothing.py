from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition = 0, fabric=None):
        super().__init__(id,condition)
        if fabric:
            self.fabric = fabric
        else:
            self.fabric = "Unknown"

#inherit get_category function from Item class, return class name   
    def get_category(self):
        return super().get_category()

#inherit str function from Item class, return string
    def __str__(self):
        return super().__str__() + f" It is made from {self.fabric} fabric."

    def condition_description(self):
        return super().condition_description()