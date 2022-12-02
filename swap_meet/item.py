import uuid


class Item:

    def __init__(self, id=None, condition=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition

    
    def get_category(self):
        """
        return class name
        """
        whoami = type(self).__name__
        return whoami
    
    def __str__(self):
        """
        return a message about the item instance
        """
        stringified = f"An object of type {self.get_category()} with id {self.id}"
        return stringified
    
    def condition_description(self):
        """
        return description of instance's condition
        """
        conditions = {
            0: "mint",
            1: "excellent",
            2: "very good",
            3: "good",
            4: "fair",
            5: "heavily used",
        }
        return conditions[round(self.condition)]
