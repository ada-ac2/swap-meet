from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, type = "Unknown", condition = 0):
        super().__init__(id, condition)
        self.type = type

    def get_attribute(self):
        return self.type

    def __str__(self):
        
        summary = super().__str__()
        class_summary = f"This is a {self.type} device."
        return ". ".join((summary, class_summary))
