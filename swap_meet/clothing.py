#import parent class 
from swap_meet.item import Item

class Clothing(Item):
    
    #apply parent class in constructor
    def __init__(self, id=None, fabric="Unknown", condition=None):
        super().__init__(id, condition)
        self.fabric=fabric
    
    #here I return the string from the parent contstructer inside of an f string with additional changes
    #Aka Override
    def __str__(self):
        return (f"{super().__str__()}. It is made from {self.fabric} fabric.")

