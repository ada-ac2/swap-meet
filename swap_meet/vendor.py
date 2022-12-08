class Vendor:
    def __init__(self, inventory=None):
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

    def swap_items(self, other_vendor, my_item, thier_item):
        #input: other_vendor: instance of another Vendor
        #       my_item: instance of an Item, what item 'this' vendor wants to swap
        #       thier_item: instance of an Item, what item other_vendor wants to swap
        #output: return True or False
        if my_item not in self.inventory or thier_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            self.inventory.append(thier_item)
            other_vendor.remove(thier_item)
            return True

    def swap_first_item(self, other_vendor):
        #If either itself or the friend have an empty `inventory`, the method returns `False`
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            #gets vendor's first item, removes it and add it to other vendor's inventory
            vendor_first_item = self.inventory.pop(0)
            other_vendor.inventory.append(vendor_first_item)

            #gets other vendor's first item, removes it and add it to vendor's inventory
            other_vendor_first_item = other_vendor.inventory.pop(0)
            self.inventory.append(other_vendor_first_item)

            return True
    
    #returns a list of objects in the inventory with that category
    #                         a string
    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.category == category:
                result.append(item)
        return result

    #get the item with the best condition in a certain category
    def get_best_by_category(self, category):
        highest_quality = 0
        high_quality_item = None
        for item in self.inventory:
            if item.category == category:
                if item.condition > highest_quality:
                    highest_quality = item.condition
                    high_quality_item = item
        return high_quality_item

    #other_vendor: Vendor instance we are trading with
    #my_priority: the vendor's category we want to receive
    #their_priority: other_vendor's category they want to receive
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_best = self.get_best_by_category(their_priority)
        thier_best = other_vendor.get_best_by_category(my_priority)

        res = self.swap_items(other_vendor, my_best, thier_best)
        return res


