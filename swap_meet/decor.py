class Decor:
    def __init__(self, id=None, width=0, length=0, condition=0):
        self.id = id if id else uuid.uuid4().int
        self.width = width
        self.length = length
        self.condition = condition

    def __str__(self):
        " "
        return (f'An object of type Decor with id {self.id}. '
                f'It takes up a {self.width} by {self.length} sized space.'
        )
    
    def get_category(self):
        return type(self).__name__