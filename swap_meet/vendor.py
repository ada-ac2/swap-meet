class Vendor:
    def __init__(self, inventory=None):

        
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None

        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.get_category() == category:
                category_items.append(item)
        
        if not category_items:
            return None
        
        return category_items

    def get_best_by_category(self, category):
        if not self.get_by_category(category):
            return None

        return max(self.get_by_category(category), key=lambda item: item.condition)

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.get_best_by_category(their_priority) or not other.get_best_by_category(my_priority):
            return False

        self.swap_items(other, self.get_best_by_category(their_priority), other.get_best_by_category(my_priority))
        return True


        



