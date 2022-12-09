from .item import Item

class Decor(Item):
    
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id, condition)
        self.width = int(width)
        self.length = int(length)


    def __str__(self):
        decor_str = (
            f"{super().__str__()}. "
            f"It takes up a {self.width} by {self.length} sized space."
        )
        return decor_str
