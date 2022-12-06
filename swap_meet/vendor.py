class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, item):
        if not item:
            return None
        self.inventory.append(item) 
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        if not id:
            return None
        return next((item for item in self.inventory if item.id == id), None)

    def swap_items(self, other_vendor, my_item, their_item):
        if not my_item or not their_item:
            return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.add(other_vendor.remove(their_item))
        other_vendor.add(self.remove(my_item))
        return True

    def swap_first_item(self, other_vendor):
        if not self or not other_vendor:
            return False
        if not self.inventory or not other_vendor.inventory:
            return False
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True
    
    def get_by_category(self, category):
        if not category:
            return None
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self, category):
        if not category:
            return None
        category_items = self.get_by_category(category)
        if not category_items:
            return None
        return max(category_items, key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
         my_best_item = self.get_best_by_category(their_priority)
         their_best_item = other_vendor.get_best_by_category(my_priority)
         if not my_best_item or not their_best_item:
            return False
         return self.swap_items(other_vendor, my_best_item, their_best_item)