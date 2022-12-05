from .item import Item

class Clothing(Item):
    
    def __init__(self, id = None, condition = None, fabric = None):
        super().__init__(id, condition)
        if fabric == None:
            self.fabric = "Unknown"
        else:
            self.fabric = fabric

    def __str__(self):
        return f"An object of type {super().get_category()} with id {str(self.id)}. It is made from {str(self.fabric)} fabric."  
