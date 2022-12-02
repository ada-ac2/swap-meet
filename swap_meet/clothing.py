from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, fabric = "Unknown", id = None, condition = 0):
        super().__init__(id, condition)
        self.fabric = fabric

    def __str__(self):
        summary = super().__str__()
        class_summary = f"It is made from {self.fabric} fabric."

        return ". ".join((summary, class_summary))