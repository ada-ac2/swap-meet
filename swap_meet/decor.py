from .item import Item

class Decor(Item):
    def __init__(self, id = None, condition = None, width = None, length = None):
        super().__init__(id, condition)
        if not width:
            self.width = 0
        else:
            self.width = width
        if not length:
            self.lenght = 0
        else:
            self.lenght = length

    def __str__(self):
        return f"An object of type {super().get_category()} with id {str(self.id)}. It takes up a {str(self.width)} by {str(self.lenght)} sized space."  
