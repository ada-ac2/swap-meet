class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item

        except ValueError:
            return None

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item

        return None

    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False

        self.remove(my_item)
        self.add(their_item)

        other.remove(their_item)
        other.add(my_item)

        return True

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        my_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_first_item, other_first_item)

    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.get_category() == category:
                result.append(item)
        
        return result

    def get_best_by_category(self, category):
        highest = 0
        best_item = None

        for item in self.inventory:
            if item.get_category() == category and item.condition > highest:
                best_item = item
                highest = item.condition

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if their_best_item is None or my_best_item is None:
            return False

        return self.swap_items(other, my_best_item, their_best_item)