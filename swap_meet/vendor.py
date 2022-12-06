class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, item):
        # Check input validation
        if not item:
            raise ValueError("Invalid Input")
        # Check duplicated item
        if item in self.inventory:
            raise ValueError(
                "Item already exist in the current inventory, item has not been added")

        self.inventory.append(item)

        return item

    def remove(self, item):
        if item not in self.inventory:
            return None

        self.inventory.remove(item)
        return item

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None  # Return None if no matching item

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        # Removes my_item from my inventory, add to other_vendor's inventory
        swap_item1 = self.remove(my_item)
        other_vendor.add(swap_item1)
        # Removes their_item from other_vendor's inventory, add to my inventory
        swap_item2 = other_vendor.remove(their_item)
        self.add(swap_item2)

        return True

    def swap_first_item(self, other_vendor):
        # Check if either vendor's inventory is empty
        if len(other_vendor.inventory) == 0 or len(self.inventory) == 0:
            return False

        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

    def get_by_category(self, category):
        result = []

        for item in self.inventory:
            item_category = item.get_category()
            if item_category == category:
                # Adds the object that has the requested category name
                result.append(item)

        return result

    def get_best_by_category(self, category):
        objects_in_category = self.get_by_category(category)
        if not objects_in_category:
            return None

        return max(objects_in_category, key=lambda object: object.condition)

        # My own logic to find the highest condition:
        # best_condition = objects_in_category[0].condition
        # best_condition_object = objects_in_category[0]
        # for object in objects_in_category:
        #     condition = object.condition
        #     if condition == 5: # Best condition is 5, no need to check for the rest
        #         return object
        #     if condition > best_condition:
        #         best_condition = condition
        #         best_condition_object = object

        # return best_condition_object

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, my_best_item, their_best_item)

    def display_inventory(self, category=""):
        if category:
            items_in_category = self.get_by_category(category)
        else:
            items_in_category = self.inventory

        if not items_in_category:
            print("No inventory to display.")
        else:
            index = 1
            for item in items_in_category:
                print(f"{index}. {item.__str__()}") 
                index += 1

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)

        return self.swap_items(other_vendor, my_item, their_item)

    def choose_and_swap_items(self, other_vendor, category=""):
        self.display_inventory(category) 
        other_vendor.display_inventory(category)

        id_to_swap = int(input("Please enter the id of the item you want to swap to: "))
        id_to_get_after_swap = int(input("Please enter the id of the item you want to get from other vendor after swap: "))

        return self.swap_by_id(other_vendor, id_to_swap, id_to_get_after_swap)


    # ***************************************
    # ****** Optional Enhancements **********
    # ***************************************
    def swap_decor_by_space(self, other_vendor): 
        for item in self.inventory: 
            my_size = item.width * item.length 
            for their_item in other_vendor.inventory:
                if my_size == their_item.width * their_item.length: 
                    self.swap_items(other_vendor, item, their_item)
                    return True 
        
        return False 

    def swap_clothings_by_fabric(self, other_vendor): 
        for item in self.inventory: 
            for their_item in other_vendor.inventory:
                if item.fabric  == their_item.fabric: 
                    self.swap_items(other_vendor, item, their_item)
                    return True 
        
        return False 

    def swap_electronics_by_type(self, other_vendor): 
        for item in self.inventory: 
            for their_item in other_vendor.inventory:
                if item.type  == their_item.type: 
                    self.swap_items(other_vendor, item, their_item)
                    return True 
        
        return False 
