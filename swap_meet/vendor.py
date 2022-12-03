class Vendor:
    def __init__(self, inventory=None):
        # set default to empty list to avoid mutable objects (e.g. lists, dicts) in parameter default assignments
        self.inventory = inventory if inventory else []

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
        # lambda filter functions - read up
        result = list(filter(lambda item: item.id == id, self.inventory))
        return result[0] if result else None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            # refactor?
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            return True
            
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            self.inventory.append(other_vendor.inventory.pop(0))
            other_vendor.inventory.append(self.inventory.pop(0))
            return True