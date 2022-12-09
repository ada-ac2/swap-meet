from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, condition = 0, type = "Unknown"):
        super().__init__(id,condition)
        self.type = type

#inherit get_category function from Item class, return class name   
    def get_category(self):
        return super().get_category()

#inherit str function from Item class, return string
    def __str__(self):
        return super().__str__() + f" This is a {self.type} device."

    def condition_description(self):
        return super().condition_description()

#return the item with similiar type
    def compare_item(self,other_item):
        if self.type == other_item.type:
            return True
        else:
            return False
