#import parent class 
from swap_meet.item import Item

class Decor(Item):
    
    #parent constructor with additional attributes
    def __init__(self, id=None, width=0, length=0, condition=None):
        super().__init__(id, condition)
        self.width = width
        self.length=length

    #override that string from parent
    def __str__(self):
        return (f"{super().__str__()}. It takes up a {self.width} by "
        f"{self.length} sized space.")