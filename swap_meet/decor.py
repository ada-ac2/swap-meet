from swap_meet.item import Item

class Decor(Item):
    """Decor class inherits id and condition from Item class and adds the
    width and length attributes.
    """

    def __init__(self, id = None, width = 0, length = 0, condition = 0):
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def get_attribute(self):
        item_size = self.width * self.length
        return item_size

    def __str__(self):
        summary = super().__str__()
        class_summary = f"It takes up a {self.width} by {self.length} sized space."
        return ". ".join((summary, class_summary))