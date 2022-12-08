import uuid
import math

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id if id else uuid.uuid4().int
        self.condition = condition
        

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"
    
    def get_category(self):
        return self.__class__.__name__

    def condition_description(self) : 
        match math.floor(self.condition):
            case 0:
                return ("Eww... You will definitely need to clean it before use")
            case 1:
                return ("I hope you like antique style...")
            case 2:
                return ("I think this one might look nice after you clean it.")
            case 3:
                return ("Not bad!!")
            case 4:
                return ("This looks almost new.")
            case other:
                return ("Fresh out of the factory. Did anyone even touch it?")
    
    def is_similar(self):
        return True
