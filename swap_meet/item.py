import uuid
import math

class Item:
    def __init__(self, id=None, condition=0):           
        self.id = id if id else uuid.uuid4().int
        if type(self.id) != int:
            raise TypeError("Id should be interger")
        self.condition = condition
        

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"
    
    def get_category(self):
        return self.__class__.__name__

    def condition_description(self) : 
        # Make sure condition is a integer between zero and five
        condition = max(0, min(5, math.floor(self.condition)))
        description_dict = {
            0: "Eww... You will definitely need to clean it before use",
            1: "I hope you like antique style...",
            2: "I think this one might look nice after you clean it.",
            3: "Not bad!!",
            4: "This looks almost new.",
            5: "Fresh out of the factory. Did anyone even touch it?"
        }
        return description_dict[condition]

    def is_similar(self):
        return True
