import uuid


class Item:

    def __init__(self, id=None):
        self.id = id if id is not None else uuid.uuid4().int
    
    def get_category(self):
        """
        return class name (Item)
        """
        whoami = type(self).__name__
        return whoami
    
    def __str__(self):
        """
        return a message about the item instance
        """
        stringified = f"An object of type Item with id {self.id}"
        return stringified
