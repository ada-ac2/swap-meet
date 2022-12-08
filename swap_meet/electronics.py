import uuid
class Electronics:
    def __init__(self, id=None, type="Unknown"):
        if id is None:
            self.id =uuid.uuid4().int
        else:
            self.id = id
        self.type = type
    def get_category(self):
        return "Electronics"
    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."
