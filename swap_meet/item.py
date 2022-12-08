import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition

    def get_category(self):
        return type(self).__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}"

    def condition_description(self):
        if self.condition == 0:
            return "New"
        elif  0<self.condition <=1:
            return "Like New"
        elif 1<self.condition <=2:
            return "Good"
        elif 2<self.condition <=3:
            return "Fair"
        elif 3<self.condition <=4:
            return "Poor"
        else:
            return "Very Poor"
