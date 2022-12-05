class Vendor:
    def __init__( self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add( self, item):
        self.inventory.append(item)
        return item

    def remove( self, item):
        if self.inventory == None or item not in self.inventory:
            return None
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, item_id):
        if not self.inventory:
            return None
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        
        if not self.inventory or \
            not other_vendor.inventory or \
            not my_item or not their_item or \
            my_item not in self.inventory or \
            their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

