class Vendor:
    def __init__(self, inventory=None):
        #checks input parameters annd setting default
        self.inventory = inventory if inventory is not None else []

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
        for item in self.inventory:
            if item.id == id:
                return item
        return None
    #            fatimah.swap_items(jolie, item_b, item_d)
    def swap_items(self, other_vendor, my_item, thier_item):
        #input: other_vendor: instance of another Vendor
        #       my_item: instance of an Item, what item 'this' vendor wants to swap
        #       thier_item: instance of an Item, what item other_vendor wants to swap
        #output: return True or False
        if (my_item not in self.inventory) or (thier_item not in other_vendor.inventory):
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            self.inventory.append(thier_item)
            other_vendor.remove(thier_item)
            return True

