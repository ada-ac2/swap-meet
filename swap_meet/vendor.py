class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return None

    def get_by_id(self, id):

        for item in self.inventory:
            if item.id == id:
                return item

        return None

    def get_by_category(self, category):
        category_items = []

        for item in self.inventory:
            if item.get_category() == category:
                category_items.append(item)
        
        return category_items


    def get_best_by_category(self, category):

        category_items = self.get_by_category(category)
        if not category_items:
            return None

        highest_value = 0
        item_to_return = None

        for item in category_items:
            if item.condition > highest_value:
                highest_value = item.condition
                item_to_return = item
        return item_to_return

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
        # if my_priority == getbestbycategory on othervendorinv
        # if their_priority == getbestbycategory on self.inventory

        # swap
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        if not their_item or not my_item:
            return False

        self.swap_items(other_vendor, my_item, their_item)
            
        return True

    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or \
            their_item not in other_vendor.inventory:
            return False

        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)

        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
            
        self.inventory.append(other_vendor.inventory[0])
        other_vendor.inventory.append(self.inventory[0])

        self.inventory.pop(0)
        other_vendor.inventory.pop(0)

        return True
    