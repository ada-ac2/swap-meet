import uuid
class Item:
    def __init__(self, id=None, condition=None): 
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        if condition:
            self.condition = condition
        else:
            self.condition = 0.0   
        
    
    def get_category(self):
        return f"{self.__class__.__name__}"
        
    def __str__(self):

        return f"An object of type Item with id {self.id}"
        
    def condition_description(self):
        if self.condition == 5:
            return "Like New" 
        elif self.condition == 4:
            return "Very Good"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 1:
            return "Poor"
        

    