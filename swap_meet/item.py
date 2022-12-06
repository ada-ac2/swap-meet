import uuid
import math
class Item:
    def __init__(self, id=None, condition=0):
        unique_identifier = uuid.uuid4()
        self.id = id if id else unique_identifier.int
        self.condition = condition if condition else 0

    def get_category(self):
        return self.__class__.__name__
        
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"

    def condition_description(self):
        condition_rating = round(self.condition)
        if condition_rating == 0:
            return "mint condition"
        elif condition_rating == 1:
            return "as good as new"
        elif condition_rating == 2:
            return "used condition"
        elif condition_rating == 3:
            return "use at your own discretion"
        elif condition_rating == 4:
            return "may not be working"
        elif condition_rating == 5:
            return "user risk involved"
        else:
            return "Unknown condition"