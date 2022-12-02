class Vendor:
    
    def __init__(self, inventory=None):
        # Inventory attribute should be optional. 
        # If there is no inventory argument was passed into. The default value of inventory will be an empty list.
        self.inventory = inventory if inventory else []
    
    def add(self, new_item):
        if not new_item:
            raise ValueError("Item can't be empty.")    
        self.inventory.append(new_item)
        return new_item

    def remove(self, item):
        # when there are two or more duplicate items in the inventory, we'll only remove one.
        try:
            self.inventory.remove(item)
            return item       
        except ValueError:  # When the item is not in inventory will raise value error.
            return None




