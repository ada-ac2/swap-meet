import uuid
from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None,):
        if inventory is None:
            self.inventory = []
        else:
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
    # need check
    def get_by_id(self, id):
        for n in self.inventory:
            if n.id == id:
                return n.id
        return None
    
    def swap_items(self, b_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in b_vendor.inventory :
            return False
        else:
            self.remove(my_item)
            b_vendor.add(my_item)
            self.add(their_item)
            b_vendor.remove(their_item)
            return True

    def swap_first_item(self,b_vendor):
        if  len(self.inventory) == 0 or len(b_vendor.inventory) == 0:
            return False
        else:
            my_item = self.inventory.pop(0)
            b_vendor.add(my_item)
            their_item = b_vendor.inventory.pop(0)
            self.add(their_item)
            return True

    def get_by_category(self, category):
        pass

    def get_best_by_category(self, category):
        pass