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


    def get_by_category(self, category):
        items_from_category = list(filter(lambda item: item.get_category().lower() == category.lower(), self.inventory))

        return items_from_category


    def get_best_by_category(self, category):
        all_items_from_category = self.get_by_category(category)
        
        return max(all_items_from_category, key = lambda item: item.condition) if all_items_from_category else None


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.get_by_category(their_priority) or not other_vendor.get_by_category(my_priority):
            return False

        else:
            self.swap_items(other_vendor, self.get_best_by_category(their_priority), other_vendor.get_best_by_category(my_priority))
            return True

    def display_inventory(self, category = ''):
        if not category and self.inventory:
            result_list = self.inventory
        elif not self.get_by_category(category) or not self.inventory:
            print("No inventory to display.")
            return False
        else:
            result_list = self.get_by_category(category)

        for i in range(len(result_list)):
            print(f"{i+1}. {result_list[i]}")
        return True

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)

        if not my_item or not their_item:
            return False

        self.swap_items(other_vendor,my_item, their_item )
        return True

    def choose_and_swap_items(self, other_vendor, category = ""):
        self.display_inventory(category = category)
        other_vendor.display_inventory(category = category)
        my_item_id = input("Please provide the ID of the item you will giving to the other vendor: ")
        other_vendor_item_id = input("Please provide the ID of the item you will be taking from the other vendor: ")
        return self.swap_by_id(other_vendor , int(my_item_id), int(other_vendor_item_id))