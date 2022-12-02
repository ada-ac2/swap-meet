import uuid
class Item:
    
    #Instantiate with id, allowing custom or using UUID Int auto generate 
    def __init__(self, id=None):
        self.id = id if id is not None else uuid.uuid1().int
    
    #get the class name 
    def get_category(self):
        return str(type(self).__name__)

    #here I am overriding the __str__ method. 
    def __str__(self):
        return (f"An object of type {self.get_category()} with id {self.id}")
    
