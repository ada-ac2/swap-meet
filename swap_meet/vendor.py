class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if not self.inventory[item]:
            return None
        else: 
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, id):
        if not self.inventory[id]:
            return None
        else:
            return self.inventory[id]