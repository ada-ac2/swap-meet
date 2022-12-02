#from .item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return None
        return item

    def get_by_id(self, id):      
        #return id if id in self.inventory else None
        for item in self.inventory:
            if id == item.id:
                return id
        return None

        