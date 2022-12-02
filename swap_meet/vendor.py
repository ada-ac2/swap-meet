from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None) :
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        if not item:
            return item

        if item not in self.inventory:
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

    def swap_items(self, other_vendor, my_item, their_item):
        if other_vendor is None or my_item is None or their_item is None:
            return False

        if my_item not in self.inventory:
            return False

        if their_item not in other_vendor.inventory:
            return False

        self.add(their_item)
        other_vendor.add(my_item)
        self.remove(my_item)
        other_vendor.remove(their_item)
        return True
