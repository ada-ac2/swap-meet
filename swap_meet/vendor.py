class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None
        else:
            self.inventory.remove(item)
            return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:            
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False        
        other_vendor.add(my_item)
        self.remove(my_item)     
        self.add(their_item)
        other_vendor.remove(their_item)    
        return True
    
    def swap_first_item(self, other_vendor):
        if not other_vendor.inventory or not self.inventory:
            return False
        first_my_item = self.remove(self.inventory[0])
        other_vendor.add(first_my_item)
        first_their_item = other_vendor.remove(other_vendor.inventory[0])
        self.add(first_their_item)
        return True
