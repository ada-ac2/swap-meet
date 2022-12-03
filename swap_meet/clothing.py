from .item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric
        self.condition = condition
    
    def __str__(self):
        return (f'An object of type Clothing with id {self.id}. ' 
                f'It is made from {self.fabric} fabric.'
        )