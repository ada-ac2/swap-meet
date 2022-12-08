from swap_meet.item import Item
class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id, condition)
        
        self.width = width
        self.length = length

    def __str__(self) -> str:
        decor_str = super().__str__()
        decor_str += f". It takes up a {self.width} by {self.length} sized space."
        return decor_str

    def get_space(self):
        return self.length, self.width