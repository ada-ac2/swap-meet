import uuid
class Item:
    
    #Instantiate with id, allowing custom or using UUID Int auto generate 
    def __init__(self, id=None, condition=None):
        self.id = id if id is not None else uuid.uuid1().int
        self.condition = condition if condition is not None else 0
    #get the class name 
    def get_category(self):
        return str(type(self).__name__)

    #here I am overriding the __str__ method. 
    def __str__(self):
        return (f"An object of type {self.get_category()} with id {self.id}")

    #adding a condition description class to describe condition based on value of condition
    def condition_description(self):
        case = lambda x: self.condition < x
        if case(1): item_condition_desc = "Very Poor Indeed"
        elif case(2): item_condition_desc = "This will likely be part of a DIY"
        elif case(3): item_condition_desc = "Not To Shabby, not to great"
        elif case(4): item_condition_desc = "Hey now, this is a tad swanky"
        elif case(5): item_condition_desc = "You find yourself a right treasure you did!"
        else  : item_condition_desc = "This is so pristine its obscene!"
        return item_condition_desc
    
