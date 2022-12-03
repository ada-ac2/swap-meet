from swap_meet.item import Item
class Electronics(Item):
    def __init__(self, id=None, type="Unknown"):
        super().__init__(id)
        self.type = type
    
    def __str__(self):
        return (f"{super().__str__()}. This is a {self.type} device.")
