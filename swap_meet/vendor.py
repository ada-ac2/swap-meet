#from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

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
        for item in self.inventory:
            if id == item.id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):       
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        other_vendor.add(self.remove(my_item))
        self.add(other_vendor.remove(their_item))

        return True
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        first_item_my_inventory = self.remove(self.inventory[0])
        first_item_other_inventory = other_vendor.remove(other_vendor.inventory[0])

        self.inventory.insert(0, first_item_other_inventory)
        other_vendor.inventory.insert(0, first_item_my_inventory)
        return True