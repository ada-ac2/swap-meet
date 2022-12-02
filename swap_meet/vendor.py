class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory 
        if type(self.inventory) is not list:
            raise TypeError("Please enter the inventory as a list.")

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return None

    def get_by_id(self, item_id):  
        specific_item = list(filter(lambda item: item.id == item_id, self.inventory))
        return specific_item[0] if specific_item else None

        # for item in self.inventory:
        #     if item.id == item_id:
        #         return item

        # return None

    def swap_items(self, other_vendor, self_item, other_vendor_item):
        if self_item in self.inventory and other_vendor_item in other_vendor.inventory:
            self.remove(self_item)
            self.add(other_vendor_item)
            other_vendor.remove(other_vendor_item)
            other_vendor.add(self_item)
            return True
        else:
            return False

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
