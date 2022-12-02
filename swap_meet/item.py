import uuid

class Item:
    
    def __init__(self, id = None, condition = 0):
        self.id = id if id is not None else uuid.uuid1().int
        self.condition = condition

    def get_category(self):
        return "Item"

    def condition_description(self):
        switch = {
            0 : "gross",
            1 : "not good",
            2 : "okay",
            3 : "good",
            4 : "not bad",
            5 : "excellent"
        }
        return switch.get(self.condition)

    def __str__(self):
        return f"An object of type Item with id {self.id}"