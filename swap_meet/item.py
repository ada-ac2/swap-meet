import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = id if id is not None else int(uuid.uuid4())
        self.condition = condition

    def __str__(self):
        return f'An object of type Item with id {self.id}'

    def get_category(self):
        return "Item"

    def condition_description(self):
        if self.condition <= 1.0:
            return 'trash'
        elif self.condition <= 2.0:
            return 'heavily used'
        elif self.condition <= 3.0:
            return 'alright'
        elif self.condition <= 4.0:
            return 'like new'
        else:
            return 'mint'