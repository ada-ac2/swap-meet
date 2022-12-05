from .item import Item

class Electronics(Item):
    def __init__(self, id = None, condition = None, type = None):
        super().__init__(id, condition)
        if not type:
            self.type = "Unknown"
        else:
            self.type = type
        
    def __str__(self):
        return f"An object of type {super().get_category()} with id {str(self.id)}. This is a {str(self.type)} device."
