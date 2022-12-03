class Clothing:
    def __init__(self, id=None, fabric="Unknown", condition=0):
        self.id = id if id else uuid.uuid4().int
        self.fabric = fabric
        self.condition = condition
    
    def __str__(self):
        return (f'An object of type Clothing with id {self.id}. ' 
                f'It is made from {self.fabric} fabric.'
        )

    def get_category(self):
        return type(self).__name__