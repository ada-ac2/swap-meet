import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        #maybe check if id already exists so that there won't be duplicates??
        self.id = uuid.uuid4().int if id is None else id
        if condition < 0 or condition > 5:
            raise ValueError("Please choose the condition of your item on a scale from 0(like new) to 5 (very bad).")
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __repr__(self):
        return f"An object of type {self.get_category()} with id {self.id}"

    def condition_description(self):
        if self.condition == 0:
            description = "like new"
        elif self.condition <= 1:
            description = "very good"
        elif self.condition <= 2:
            description = "good"
        elif self.condition <= 3:
            description = "okay"
        elif self.condition <= 4:
            description = "bad"
        elif self.condition <= 5:
            description = "very bad"

        return description