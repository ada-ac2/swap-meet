from .item import Item
class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    def remove(self, item):  
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else: 
            return None
    def get_by_id(self,id):
        for item in self.inventory:
            if item.id  == id:
                return item
        return 
 
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False
