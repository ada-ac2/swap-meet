import uuid
import math 

class Item:
    def __init__(self, id=None, condition=0):
        if id and not isinstance(id, int):
            raise ValueError("ID must be an integer.")

        self.id = id if id else uuid.uuid1().int
        self.condition = condition

    def get_category(self):
        return type(self).__name__

    def condition_description(self):
        # Round up condition if it is not an integer 
        condition = math.floor(self.condition) 
        if condition == 0:
            return "New"
        if condition == 1:
            return "Close to new"
        if condition == 2 or self.condition == 3:
            return "Normal Wear"
        if condition == 4:
            return "Used"
        else:
            return "Heavily Used"

    # Override str from python built-in
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"
