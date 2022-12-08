import uuid
class Decor:
    def __init__(self, id=None, width=0, length=0):
        if id is None:
            self.id =uuid.uuid4().int
        else:
            self.id = id
        self.width = width
        self.length = length
    def get_category(self):
        return "Decor"
    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."