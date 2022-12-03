class Electronics:
    def __init__(self, id=None, type="Unknown", condition=0):
        self.id = id if id else uuid.uuid4().int
        self.type = type
        self.condition = condition
    
    def __str__(self):
        return (f'An object of type Electronics with id {self.id}. '
                f'This is a {self.type} device.'
        )

    def get_category(self):
        return type(self).__name__
