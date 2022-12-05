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

    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        return self.swap_items(other_vendor, my_first_item, their_first_item)
        

    def get_by_category(self, category):
        inventory_with_category = []
        for item in self.inventory:
            if item.get_category() == category:
                inventory_with_category.append(item)
        return inventory_with_category
    
    def get_best_by_category(self, category):
        cur_best_item = None
        cur_best_condition = None
        for item in self.inventory:
            if item.get_category() == category:
                if cur_best_item is None or item.condition > cur_best_condition:
                    cur_best_item = item
                    cur_best_condition = item.condition
        return cur_best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item and their_priority:
            return self.swap_items(other_vendor, my_best_item, their_best_item)
        return False
    
    def display_inventory(self, category=""):
        assigned_category_inventory = []
        if not category:  # When there is no assigned category, it should display all inventory
            assigned_category_inventory = list(self.inventory)
        
        for item in self.inventory:
            if item.get_category() == category:
                assigned_category_inventory.append(item)
        

        if not assigned_category_inventory:
            print("No inventory to display.")
        
        count = 1
        for item in assigned_category_inventory:
            print(f"{count}. {item.__str__()}")
            count += 1
    
    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)

        return self.swap_items(other_vendor, my_item, their_item)












