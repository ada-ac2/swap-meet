class Vendor:
    def __init__(self, inventory=None):
        # set default to empty list to avoid mutable objects (e.g. lists, dicts) in parameter default assignments
        self.inventory = inventory if inventory else []

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return None
    
    def get_by_id(self, id):
        # lambda filter functions - read up
        result = list(filter(lambda item: item.id == id, self.inventory))
        return result[0] if result else None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            # refactor?
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            return True
            
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        
    def get_by_category(self, category):
        result = list(
            filter(lambda item: item.get_category() == category, self.inventory)
        )
        return result
    
    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if items:
            result = max(items, key=lambda item: item.condition)
            return result
        return None

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_for_other = self.get_best_by_category(their_priority)
        their_best_for_me = other_vendor.get_best_by_category(my_priority)
        if not my_best_for_other or not their_best_for_me:
            return False
        else:
            self.swap_items(other_vendor, my_best_for_other, their_best_for_me)
            return True
        
    def display_inventory(self, category=''):
        if not self.inventory:
            print('No inventory to display.')
        else:
            ### what is wrong here ??????
            items = [self.get_by_category(category) if category else self.inventory]
            [print(item) for item in items]

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_item = self.get_by_id(my_item_id) 
        their_item = other_vendor.get_by_id(their_item_id)
        if not my_item or not their_item:
            return False
        else:
            self.swap_items(other_vendor, my_item, their_item)
            return True

    def choose_and_swap_items(self, other_vendor, category=''):
        [vendor.display_inventory(category) for vendor in [self, other_vendor]]
        my_item_id = input('Please input the item ID you would like to give to the other vendor: ')
        their_item_id = input('Please input the item ID you would like to take from the other vendor: ')
        return True if self.swap_by_id(other_vendor, my_item_id, their_item_id) else False

# debugging
from .clothing import Clothing
from .electronics import Electronics
from .decor import Decor
from .item import Item
item_a = Clothing(id=123, fabric="Striped")
item_b = Electronics(id=456, type="Handheld Game")
item_c = Decor(id=789, width=2, length=4)
item_d = Item(id=100)
vendor = Vendor(inventory=[item_a, item_b, item_c, item_d])
vendor.display_inventory()
