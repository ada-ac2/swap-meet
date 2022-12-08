class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if not inventory else inventory

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
            return []

        item_category_list = list(filter(lambda item: item.get_category() == category, self.inventory))
        return item_category_list

    def get_best_by_category(self, category):
        item_category_list = self.get_by_category(category)
        if not item_category_list:
            return None

        max_item = max(item_category_list, key=lambda item: item.condition)
        return max_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.inventory or not other_vendor.inventory:
            return False
        their_priority_item_in_my_inventory = self.get_best_by_category(their_priority)
        my_priority_item_in_their_inventory = other_vendor.get_best_by_category(my_priority)
        if my_priority_item_in_their_inventory == None or their_priority_item_in_my_inventory == None:
            False
        return self.swap_items(other_vendor, their_priority_item_in_my_inventory, my_priority_item_in_their_inventory)
    
    def display_inventory(self, category=""):
        if not self.inventory:
            print("No inventory to display.")
            return

        if not category:
            print_inventory(self.inventory)
            return

        category_based_inventory = self.get_by_category(category)
        if not category_based_inventory:
            print("No inventory to display.")
            return

        print_inventory(category_based_inventory)
        return

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        if my_item_id == their_item_id:
            return False
        
        my_item = item_with_matching_id(self.inventory, my_item_id)
        their_item = item_with_matching_id(other_vendor.inventory, their_item_id)
        if not my_item or not their_item:
            return False

        self.swap_items(other_vendor, my_item, their_item)
        return True

    def choose_and_swap_items(self, other_vendor, category=""):
        print("**Vendor 1**")
        self.display_inventory(category=category)
        user_vendor_1_id = input("Choose an item based on id")
        print("**Vendor 2**")
        other_vendor.display_inventory(category=category)
        user_vendor_2_id = input("Choose an item based on id")
        print("userid", user_vendor_1_id, user_vendor_2_id)
        return self.swap_by_id(other_vendor, int(user_vendor_1_id), int(user_vendor_2_id))

def print_inventory(inventory):
    inventory_item = 1
    for item in inventory:
        print(f"{inventory_item}. {str(item)}")
        inventory_item += 1
    return

def item_with_matching_id(inventory, item_id):
    matching_item = 0
    for item in inventory:
        if item.id == item_id:
            matching_item = item
    return matching_item