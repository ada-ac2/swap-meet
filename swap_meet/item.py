import uuid

class Item:
    def __init__(self, id=None, condition=0) -> None:            
        self.id = id if id else uuid.uuid4().int
        self.condition = condition

    def get_category(self):
        return type(self).__name__

    def __str__(self) -> str:
        return f"An object of type {self.get_category()} with id {self.id}"

    def condition_description(self):
        if 0 <= self.condition < 1:
            return "Terrible"
        elif 1 <= self.condition < 2:
            return "Bad"
        elif 2 <= self.condition < 3:
            return "Okay"
        elif 3 <= self.condition < 4:
            return "Good"
        elif 4 <= self.condition < 5:
            return "Great"
        elif self.condition >= 5:
            return "Amazing"