from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id = None, condition = 0, width = 0, length = 0):
        super().__init__(id, condition)
        self.width = width
        self.length = length

#inherit get_category function from superclass Item, return class name
    def get_category(self):
        return super().get_category()

#inherit str function from superclass Item, return string
    def __str__(self):
        return super().__str__() + f" It takes up a {self.width} by {self.length} sized space."

    def condition_description(self):
        return super().condition_description()

#return the item with similiar space used
    def compare_item(self, other_item):
        #if self.width == other_item.width and self.length == other_item.length:
            #return True
        if abs(self.width-other_item.width) <=2 and abs(self.width-other_item.width) <=2:
            return True
        else:
            return False
        