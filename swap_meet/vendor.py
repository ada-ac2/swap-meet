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
        found_mine = self.get_by_id(my_item.id)
        found_theirs = other_vendor.get_by_id(their_item.id)
        if found_mine is not None and found_theirs is not None:
            other_vendor.add(self.remove(my_item))
            self.add(other_vendor.remove(their_item))
            swapped = True
        return swapped