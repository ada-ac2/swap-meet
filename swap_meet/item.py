import uuid

class Item:
    def __init__(self, id=None, condition=None):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = 0 if condition is None else condition

    def __str__(self):
        return f"An object of type Item with id {str(self.id)}"

    def get_category(self):
        return self.__class__.__name__
    
    def condition_description(self):
        if 0 <= self.condition <= 1:
            return "Very bad."
        elif 1 < self.condition <= 2:
            return "Bad."
        elif 2 < self.condition <= 3:
            return "Fair."
        elif 3 < self.condition <= 4:
            return "Good"
        elif 4 < self.condition <= 5:
            return "Very good."

   