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

        # for item in self.inventory:
        #     if item.id == id:
        #         return item
        # item = list(filter(lambda x: x.id == id, self.inventory))[0]
        # return item if item else None

        item = next((i for i in self.inventory if i.id == id), None)

        return item

    def get_by_category(self, category):

        items = [i for i in self.inventory if i.get_category() == category]

        return items

        # category_items = []

        # for item in self.inventory:
        #     if item.get_category() == category:
        #         category_items.append(item)
        
        # return category_items


    def get_best_by_category(self, category):

        items = self.get_by_category(category)
        
        if not items:
            return None

        max_value = max([i.condition for i in items])

        item = next((i for i in items if i.condition == max_value), None)

        return item

        # highest_value = 0
        # item_to_return = None

        # for item in category_items:
        #     if item.condition > highest_value:
        #         highest_value = item.condition
        #         item_to_return = item
        # return item_to_return

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        if not their_item or not my_item:
            return False

        self.swap_items(other_vendor, my_item, their_item)
            
        return True

    # Optional get_by method

    def get_by_category_attribute(self, category, attribute):

        category_items = self.get_by_category(category)

        items = [item for item in category_items if attribute == item.get_attribute()]

        return items

    # Optional swap method

    def swap_by_attribute(self, other_vendor, category, attribute):
        my_items = self.get_by_category_attribute(category, attribute)
        their_items = other_vendor.get_by_category_attribute(category, attribute)
        
        my_item = my_items[0]
        their_item = their_items[0]
        
        swapped = swapped = self.swap_items(other_vendor, my_item, their_item)

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

        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        swapped = self.swap_items(other_vendor, my_item, their_item)

        return swapped

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)

        if not their_item or not my_item:
            return False

        swapped = self.swap_items(other_vendor, my_item, their_item)
            
        return swapped

    def choose_and_swap_items(self, other_vendor, category = ''):
        
        self.display_inventory(category)
        other_vendor.display_inventory(category)

        my_item_id = int(input('Enter item from your inventory by id: '))
        their_item_id = int(input('Enter item from their inventory by id: '))

        swapped = self.swap_by_id(other_vendor, my_item_id, their_item_id)

        return swapped


    def display_inventory(self, category = ''):
        
        # Refactored

        if not self.inventory:
            print("No inventory to display.")
            return

        items = self.get_by_category(category) if category else self.inventory

        if items:
            for i, item in enumerate(items, 1):
                print(f"{i}. {str(item)}")
        else: 
            print("No inventory to display.")

        # if not self.inventory:
        #     print("No inventory to display.")
        #     return

        # if category:
        #     items = self.get_by_category(category)
        #     if items:
        #         for i in range(len(items)):
        #             print(f"{i + 1}. {str(items[i])}")
        #     else: 
        #         print("No inventory to display.")
        # else:
        #     for i in range(len(self.inventory)):
        #         print(f"{i + 1}. {str(self.inventory[i])}")