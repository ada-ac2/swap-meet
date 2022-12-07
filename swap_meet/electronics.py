from .item import Item


class Electronics(Item):
    def __init__(self, id=None, condition=0, type="Unknown"):
        super().__init__(id, condition)
        self.type = type
        self.condition = condition

    def __str__(self):
        return (f'An object of type Electronics with id {self.id}. '
                f'This is a {self.type} device.'
                )
