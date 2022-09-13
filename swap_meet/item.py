import uuid

class Item:
    def __init__(self, id=None, condition=0):
        if id == None:
            self.id = uuid.uuid1().int
        else:
            self.id=id
        self.condition=condition

    def get_category(self):
        return type(self).__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"

    def condition_description(self):
        if self.condition < 3:
            return "bad"
        else:
            return "good"