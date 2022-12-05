#Wave 2 , 5
import uuid
#from swap_meet.vendor import Vendor
class Item:
    def __init__(self,id = None,category = "", condition = 0 ):
        if id is None :
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
        self.category = category

    def get_category(self):
        return self.__class__.__name__#type(self).__name__
# Wave 3
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"
# Wave 5
    def condition_description(self):
        description_of_condition = ["Mint","Heavily Used","Like New","Best Used","Gently Used","New"]
        return description_of_condition[self.condition]
    
    
