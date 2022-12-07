from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, condition=None, type=None):
        super().__init__(id, condition)
        self.type = "Unknown" if type is None else type

    def get_category(self):
        return super().get_category()

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

    def condition_description(self):
        return super().condition_description()