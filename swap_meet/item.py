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

    def condition_description(self):
        match math.floor(self.condition):
            case 0:
                return ("condition is 0")
            case 1:
                return ("condition is 1")
            case 2:
                return ("condition is 2")
            case 3:
                return ("condition is 3")
            case 4:
                return ("condition is 4")
            case other:
                return ("Lucky one with best condition")
    
    def is_similar(self):
        return True
