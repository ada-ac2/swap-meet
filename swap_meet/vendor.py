class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return None

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory or their_item not in other_vendor.inventory):
            return False
        else:
            #using pop to return removed items and store in swapped_item vars
            my_swapped_item = self.inventory.pop(self.inventory.index(my_item))
            their_swapped_item = other_vendor.inventory.pop(other_vendor.inventory.index(their_item))
            
            other_vendor.inventory.append(my_swapped_item)
            self.inventory.append(their_swapped_item)
            return True