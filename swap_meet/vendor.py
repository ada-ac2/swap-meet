#from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return None
        return item

    def get_by_id(self, id):      
        for item in self.inventory:
            if id == item.id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):       
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        other_vendor.add(self.remove(my_item))
        self.add(other_vendor.remove(their_item))

        return True
        
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        result = self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return result

    def get_by_category(self, category):
        category_list = []

        for item in self.inventory:
            if category == item.get_category():
                category_list.append(item)

        return category_list

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        
        return None if len(category_list) == 0 \
               else max(category_list, key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        get_best_by_my_category = self.get_best_by_category(their_priority)
        
        get_best_by_their_category = other_vendor.get_best_by_category(my_priority)

        result = self.swap_items(other_vendor, get_best_by_my_category, get_best_by_their_category)
        return result