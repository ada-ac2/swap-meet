from swap_meet import conditions
import uuid


class Item:
    def __init__(self, id=None, condition=0):
        self.id = self.check_valid_id(id) if id else uuid.uuid4().int
        self.condition = condition

    def __str__(self):
        return f'An object of type Item with id {self.id}'

    def get_category(self):
        return type(self).__name__

    def condition_description(self):
        return conditions[self.condition]

    def check_valid_id(self, id):
        if type(id) == int:
            return id
        elif str(id).isnumeric():
            return int(id)
        else:
            raise ValueError('id needs to be an integer value')
