import uuid

class Item:
    
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        #refactor validation of condition
        self.condition = condition
        if 0 <= self.condition <= 5:
            self.condition = float(condition)
        else:
            raise ValueError("Condition must range from 0-5.")

    def get_category(self):
        return f"{self.__class__.__name__}"

    def __str__(self):
        item_summary = f"An object of type {self.get_category()} with id {self.id}"
        return item_summary

    def condition_description(self):
        if self.condition == 0:
            return "This one should probably just go for parts..."
        elif self.condition <= 1:
            return "This item is barely holding it together"
        elif self.condition <= 2:
            return "Not the newest or the shiniest, but it'll do"
        elif self.condition <= 3:
            return "Well loved, AKA just slightly worn out"
        elif self.condition <= 4:
            return "Great condition with only minor shows of wear"
        elif self.condition <= 5:
            return "Perfect condition!"
        