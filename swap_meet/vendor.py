from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None) :
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        if not item:
            return item

        self.inventory.append(item)
        return item

    def remove(self, item):  
        if not item:
            return item

        if item not in self.inventory:
            return None

        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item

        return None