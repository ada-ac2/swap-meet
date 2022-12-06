class Vendor:
    def __init__(self, inventory=[]):
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
        if my_item == their_item:
            return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        self.add(their_item)

        other_vendor.remove(their_item)
        other_vendor.add(my_item)
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        if self.inventory[0] == other_vendor.inventory[0]:
            return False
        
        my_first_item = self.inventory[0]
        self.inventory[0] = other_vendor.inventory[0]
        other_vendor.inventory[0] = my_first_item
        return True

    def get_by_category(self, category):
        if not self.inventory:
            raise ValueError("Empty Inventory")

        item_category_list = list(filter(lambda item: item.get_category() == category, self.inventory))
        return item_category_list

    def get_best_by_category(self, category):
        item_category_list = self.get_by_category(category)
        if not item_category_list:
            return None

        max_item = max(item_category_list, key=lambda item: item.condition)
        return max_item

    def swap_best_by_category(self):
        # use swap_items
        pass