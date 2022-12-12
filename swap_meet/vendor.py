class Vendor:
    """Vendor class contains an inventory list of Item objects and methods to
    add, remove, retrieve, and swap items with other vendor instances.
    """

    def __init__(self, inventory = None):
        """Creates Vendor instance"""
        
        self.inventory = inventory if inventory is not None else []
    
    def add(self, item):
        """Adds items to inventory. Returns item."""
        
        self.inventory.append(item)
        return item

    def remove(self, item):
        """Removes item from inventory. Returns removed item or None if item
        not found.
        """

        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return None

    def get_by_id(self, id):
        """Gets item by item id from list of inventory. Returns Item object."""

        item = next((item for item in self.inventory if item.id == id), None)
        return item

    def get_by_category(self, category):
        """Gets items in inventory that match category. Returns a list."""

        inventory = self.inventory
        items = [item for item in inventory if item.get_category() == category]
        return items

    def get_best_by_category(self, category):
        """Gets item with the best condition in category from inventory. Returns
        Item object.
        """

        items = self.get_by_category(category)
        
        if not items:
            return None

        max_value = max([item.condition for item in items])
        
        item = next(
            (item for item in items if item.condition == max_value), None)
        
        return item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """Swaps best items in category from two vendors. Returns boolean."""

        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)
        
        if not their_item or not my_item:
            return False
        
        swapped = self.swap_items(other_vendor, my_item, their_item)
        return swapped

    def get_by_category_attribute(self, category, attribute):
        """Gets items from inventory that match category and item attribute.
        Returns a list.
        """

        category_items = self.get_by_category(category)
        items = [item for item in category_items 
                if attribute == item.get_attribute()]
        
        return items

    def swap_by_attribute(self, other_vendor, category, attribute):
        """Swaps items that match category and item attribute from 2 vendors.
        Returns boolean.
        """

        my_items = self.get_by_category_attribute(category, attribute)
        their_items = other_vendor.get_by_category_attribute(
                category, attribute)

        if not their_items or not my_items:
            return False
        
        my_item = my_items[0]
        their_item = their_items[0]
        swapped = self.swap_items(other_vendor, my_item, their_item)
        return swapped

    def swap_items(self, other_vendor, my_item, their_item):
        """Swaps items from 2 vendors. Returns boolean."""

        inventory = self.inventory
        if my_item not in inventory or their_item not in other_vendor.inventory:
            return False
        
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True

    def swap_first_item(self, other_vendor):
        """Swaps first item in inventory from 2 vendors. Returns boolean."""

        if not self.inventory or not other_vendor.inventory:
            return False

        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]
        swapped = self.swap_items(other_vendor, my_item, their_item)
        return swapped

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        """Swaps items by id from 2 vendors. Returns boolean."""

        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)

        if not their_item or not my_item:
            return False

        swapped = self.swap_items(other_vendor, my_item, their_item)
        return swapped

    def choose_and_swap_items(self, other_vendor, category = ""):
        """Displays inventory from 2 vendors and allows user to select items to
        swap by id. Returns boolean.
        """
        
        self.display_inventory(category)
        other_vendor.display_inventory(category)

        my_item_id = int(input("Enter item from your inventory by id: "))
        their_item_id = int(input("Enter item from their inventory by id: "))
        swapped = self.swap_by_id(other_vendor, my_item_id, their_item_id)
        return swapped

    def display_inventory(self, category = ""):
        """Displays Vendor inventory with item descriptions."""
        
        if not self.inventory:
            print("No inventory to display.")
            return

        items = self.get_by_category(category) if category else self.inventory
        if items:
            for i, item in enumerate(items, 1):
                print(f"{i}. {str(item)}")
        else: 
            print("No inventory to display.")