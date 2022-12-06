from swap_meet.item import Item
class Decor(Item):
    def __init__(self, id=None, width=0, length=0, condition=0):
        super().__init__(id, condition)
        self.width = width if width else 0
        self.length = length if length else 0

    def get_category(self):
        return f"Decor"

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}. It takes up a {self.width} by {self.length} sized space."