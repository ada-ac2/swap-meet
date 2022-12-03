from .item import Item
class Vendor:

    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []
    
    def add(self, item):
        """
        add an item to the inventory
        return added item
        """
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        """
        remove an item from inventory
        return removed item or None if not found
        """
        removed = item
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            removed = None
        return removed
    
    def get_by_id(self, id):
        """
        find if item of an given id exist in inventory
        return found item or None
        """
        found = None
        for item in self.inventory:
            if item.id == id:
                found = item
        return found

    def swap_items(self, other_vendor, my_item, their_item):
        """
        swap given items between my inventory and other vendor
        return True if targeted items exist and swapped, False otherwise
        """
        swapped = False
        found_mine = None if my_item is None else self.get_by_id(my_item.id)
        found_theirs = None if their_item is None else other_vendor.get_by_id(their_item.id)
        if found_mine is not None and found_theirs is not None:
            other_vendor.add(self.remove(my_item))
            self.add(other_vendor.remove(their_item))
            swapped = True
        return swapped
    
    def swap_first_item(self, other_vendor):
        """
        swap first item of inventory from self and other vendor
        return True if both inventories are not empty and swapped, False otherwise
        """
        swapped = False
        if self.inventory and other_vendor.inventory:
            other_vendor.add(self.remove(self.inventory[0]))
            self.add(other_vendor.remove(other_vendor.inventory[0]))
            swapped = True
        return swapped
    
    def get_by_category(self, category):
        """
        return a list of item from inventory of given category
        return empty list if no item in the inventory is of the give category
        """
        items = list()
        for item in self.inventory:
            if item.get_category() == category:
                items.append(item)
        return items
    
    def get_best_by_category(self, category):
        # I was thinking implement it with only lambda function, but couldn't figure out how to :/
        items = self.get_by_category(category)
        if items == []:
            item = None
        else:
            item = max(items, key=lambda i: i.condition)
            if item == []:
                item = None
        return item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        i_have = self.get_best_by_category(their_priority)
        vendor_has = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, i_have, vendor_has)
