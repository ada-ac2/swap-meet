import uuid 

class Item:
    def __init__(self, id = None, condition = 0):
        self.id = id if id else uuid.uuid1().int
        self.condition = condition 

    def get_category(self): 
        return type(self).__name__

    def condition_description(self):
        if self.condition == 0:
            return "New"
        if self.condition == 1:
            return "Close to new"
        if self.condition == 2 or self.condition == 3:
            return "Normal Wear"
        if self.condition == 4:
            return "Used"
        else:
            return "Heavily Used"

    # Override str from python built-in  
    def __str__(self): 
        return f"An object of type {self.get_category()} with id {self.id}"
