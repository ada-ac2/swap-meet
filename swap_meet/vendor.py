class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory else [] 
    
    def add(self, item): 
        # Check input validation 
        if not item: 
            raise ValueError("Invalid Input")
        # Check duplicated item 
        if item in self.inventory: 
            raise ValueError("Item already exist in the current inventory, item has not been added")

        self.inventory.append(item) 

        return item 

    def remove(self, item): 
        if item not in self.inventory: 
            return None 
            
        self.inventory.remove(item)
        return item 

    def get_by_id(self, item_id): 
        for item in self.inventory: 
            if item.id == item_id:
                return item
        return None # Return None if no matching item 

    def swap_items(self, other_vendor, my_item, their_item): 
        if my_item not in self.inventory or their_item not in other_vendor.inventory: 
            return False 

        # Removes my_item from my inventory, add to other_vendor's inventory 
        swap_item1 = self.remove(my_item) 
        other_vendor.add(swap_item1) 
        # Removes their_item from other_vendor's inventory, add to my inventory 
        swap_item2 = other_vendor.remove(their_item) 
        self.add(swap_item2)
        
        return True 

    def swap_first_item(self, other_vendor): 
        # Check if either vendor's inventory is empty 
        if len(other_vendor.inventory) == 0 or len(self.inventory) == 0:
            return False 
            
        # Removes the first item from both vendors' inventory 
        other_first_item = other_vendor.remove(other_vendor.inventory[0])
        my_first_item = self.remove(self.inventory[0])
        # Add/Swap items 
        self.add(other_first_item)
        other_vendor.add(my_first_item)

        return True 




