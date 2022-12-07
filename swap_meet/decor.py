from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, condition=None, width=None, length=None):
        super().__init__(id, condition)
        self.width = 0 if width is None else width
        self.length = 0 if length is None else length

    def get_category(self):
        return super().get_category()

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."

    def condition_description(self):
        return super().condition_description()