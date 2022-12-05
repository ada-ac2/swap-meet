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
