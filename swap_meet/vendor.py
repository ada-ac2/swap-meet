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
        """
        return None if inventory is empty or no such category DNE in the inventory
        else return the first best conditioned item of the category
        """
        items = self.get_by_category(category)
        if not items:
            item = None
        else:
            item = max(items, key=lambda i: i.condition)
            if not item:
                item = None
        return item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """
        find best conditioned item of given category of each person (self vendor, other vendor)
        if desired items are in eachother's inventory, swap them
        if any items not exist or inventory empty, return None
        """
        i_have = self.get_best_by_category(their_priority)
        vendor_has = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, i_have, vendor_has)
    
    def display_inventory(self, category=None):
        items = list()
        if category is None:
            items = self.inventory
            # items = [item1, item2, item3]
        else:
            items = self.get_by_category(category)
        result = ''
        if items:
            for ind, item in enumerate(items):
                if item is not None:
                    result += '{}. {}\n'.format(ind+1, item.__str__())
        else:
            result = "No inventory to display."
        print(result)

"""
if __name__ == "__main__":
    from clothing import Clothing
    from electronics import Electronics
    from decor import Decor


    item_a = Clothing(id=123, fabric="Striped")
    item_b = Electronics(id=456, type="Handheld Game")
    item_c = Decor(id=789, width=2, length=4)
    item_d = Item(id=100)
    vendor = Vendor(
        inventory=[item_a, item_b, item_c, item_d]
    )

    vendor.display_inventory()"""