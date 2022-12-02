from .item import Item
class Vendor:
    def __init__(self, inventory = None,):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        #self.item = item

    
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
        for item in self.inventory:
            if id == item.id:
                return item.id
            else:
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

