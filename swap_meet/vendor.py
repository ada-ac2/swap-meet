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

    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory or their_item not in other_vendor.inventory):
            return False
        else:
            #using pop to return removed items and store in swapped_item vars
            my_swapped_item = self.inventory.pop(self.inventory.index(my_item))
            their_swapped_item = other_vendor.inventory.pop(other_vendor.inventory.index(their_item))

            other_vendor.inventory.append(my_swapped_item)
            self.inventory.append(their_swapped_item)
            return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            my_first_item = self.inventory.pop(0)
            their_first_item = other_vendor.inventory.pop(0)

            other_vendor.inventory.append(my_first_item)
            self.inventory.append(their_first_item)
            return True

    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)
        return items_in_category

    def get_best_by_category(self, category):
        sorted_category_items = self.get_by_category(category)
        if not sorted_category_items:
            return None
        else:
            #is there a way to access the item's condition without a lambda fn here?
            return max(sorted_category_items, key=lambda item: item.condition)

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        item_for_me = other_vendor.get_best_by_category(my_priority)
        item_for_them = self.get_best_by_category(their_priority)

        return self.swap_items(other_vendor, item_for_them, item_for_me)

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)
        return self.swap_items(other_vendor, my_item, their_item)

    def choose_and_swap_items(self, other_vendor, category=""):
        self.display_inventory(category)
        other_vendor.display_inventory(category)
        my_item_id = int(input("Enter the id of your item to be swapped: "))
        their_item_id = int(input("Enter the id of the other vendor's item to be swapped: "))
        return self.swap_by_id(other_vendor, my_item_id, their_item_id)
        

    def display_inventory(self, category=""):
        #populate inventory summaries
        inventory_summaries = ""
        if not category:
            for i in range(len(self.inventory)):
                inventory_summaries += f"{i+1}. {self.inventory[i].__str__()}\n"
        else:
            items = 0
            for i in range(len(self.inventory)):
                if self.inventory[i].get_category() == category:
                    inventory_summaries += f"{items+1}. {self.inventory[i].__str__()}\n"
                    items += 1

        if inventory_summaries == "":
            print("No inventory to display.")
        else:
            print(inventory_summaries, end="")