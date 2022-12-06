from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

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

    def swap_items(self, other_vendor, my_item, their_item):
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
        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
        return True

    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]
        
    
    def get_best_by_category(self, category):
        new_inventory = self.get_by_category(category)
        if not new_inventory:
            return None
        return max(new_inventory, key = lambda item: item.condition)
            

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item =  self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if not my_best_item or not their_best_item:
            return False
        self.swap_items(other_vendor, my_best_item, their_best_item)
        return True

#work on this
    def display_inventory(self, category = ""):
        if not self.inventory:
            print("No inventory to display.")
        else:   
            if category == "":
                inventory_to_print = self.inventory
            else:
                if self.get_by_category(category):
                    inventory_to_print = self.get_by_category(category)
                else:
                    print("No inventory to display.") 
                    return

            for index in range(len(inventory_to_print)):
                print(f"{index+1}. " + str(inventory_to_print[index]))

        

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        their_item = other_vendor.get_by_id(their_item_id)
        my_item = self.get_by_id(my_item_id)
        if not my_item or not their_item:
            return False
        return self.swap_items(other_vendor, my_item, their_item)

# work on this function
    def choose_and_swap_items(self, other_vendor, category = ""):
        self.display_inventory(category)
        other_vendor.display_inventory(category)
        my_item_id = int(input("Please enter the ID of the first item you wish to swap: "))
        vendor_item_id = int(input("Please enter the ID of the second item you wish to swap: "))
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(vendor_item_id)

        if my_item and their_item:
            return self.swap_items(other_vendor, my_item, their_item)
        else:
            return False