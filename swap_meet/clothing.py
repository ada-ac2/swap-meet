from .item import Item 

class Clothing(Item):
    def __init__(self, id=None, fabric = "Unknown", condition = 0):
        super().__init__(id, condition)
        self.fabric = fabric 
    
    def get_category(self):
        return super().get_category() 
    
    def __str__(self):
        return f"{super().__str__()}. It is made from {self.fabric} fabric."
    

