from .item import Item 

class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id, condition)
        self.width = width 
        self.length = length

    def get_category(self):
        return super().get_category() 
    
    def __str__(self):
        return f"{super().__str__()}. It takes up a {self.width} by {self.length} sized space."
    