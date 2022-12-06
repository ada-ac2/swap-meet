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
        result = list(filter(lambda item: item.id == id, self.inventory))
        return result[0] if result else None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
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
    
    def get_best_by_category(self, category=None, list=None):
        items = list if list else self.get_by_category(category)
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
        items = self.get_by_category(category) if category else self.inventory
        if items:
            [print(f'{i}. {item}') for i, item in enumerate(items, 1)]
        else:
            print('No inventory to display.')

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
        my_item_id = int(input('Please input the item ID you would like to give to the other vendor: '))
        their_item_id = int(input('Please input the item ID you would like to take from the other vendor: '))
        return True if self.swap_by_id(other_vendor, my_item_id, their_item_id) else False

    def get_by_category_attribute(self, category, attribute, val):
        items = self.get_by_category(category)
        items_by_attr = []
        for item in items:
            if val == getattr(item, attribute):
                items_by_attr.append(item)
        return items_by_attr
    
    def swap_by_category_attribute(self, other_vendor, category, attribute, attr_val):
        my_items = self.get_by_category_attribute(category, attribute, attr_val)
        their_items = other_vendor.get_by_category_attribute(category, attribute, attr_val)
        result = self.swap_items(
            other_vendor,
            self.get_best_by_category(list=my_items),
            other_vendor.get_best_by_category(list=their_items)
        )
        return result
