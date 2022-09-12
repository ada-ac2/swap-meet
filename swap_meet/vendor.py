class Vendor:
    def __init__(self, inventory=None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

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

        # get first item   
        my_first_item = self.inventory[0]
        other_first_item = other_vendor.inventory[0]

        # swap
        self.inventory = self.inventory[1:]
        other_vendor.inventory = other_vendor.inventory[1:]

        self.inventory.append(other_first_item)
        other_vendor.inventory.append(my_first_item)

        return True