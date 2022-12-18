#Wave 2 , 5
from math import floor
import uuid
#from swap_meet.vendor import Vendor
class Item:
    def __init__(self, id = None, category = "", condition = 0):
        
        if id is not None and not isinstance(id,int):
            raise ValueError("ID must be an integer")
        self.id = id if id else uuid.uuid4().int
        self.condition = condition 
        self.category = category

    def get_category(self):
        return self.__class__.__name__#type(self).__name__ I would like to know which is best practice in these two
    

# Wave 3
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"

# Wave 5
    def condition_description(self):
        description_of_condition = ["Mint","Heavily Used","Like New","Gently Used","Best Used","New"]
        
        return description_of_condition[round(self.condition)]
    
    
