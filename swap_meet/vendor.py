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
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        removed_my_item = self.remove(my_item)
        removed_their_item = other_vendor.remove(their_item)

        if removed_my_item and removed_their_item:
            self.add(their_item)
            other_vendor.add(my_item)
            return True
        if removed_my_item:
            self.add(my_item)
        if removed_their_item:
            other_vendor.add(their_item)
        return False
        







