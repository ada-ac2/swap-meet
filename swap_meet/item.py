import uuid

class Item:    
    def __init__(self, id=None, condition=0):
        if not id:
            id = uuid.uuid4().int
        self.id = id
        self.condition = condition
    
    def get_category(self):
        return f'{self.__class__.__name__}'

    def __str__(self):
        return f"An object of type Item with id {self.id}"
    
    def condition_description(self):
        if self.condition == 0:
            return f'Heavily used'
        elif self.condition == 1:
            return f'Acceptable'
        elif self.condition == 2:
            return f'Good'
        elif self.condition == 3:
            return f'Very good'
        elif self.condition == 4:
            return f'Like new'
        else:
            return f"Brand New"


