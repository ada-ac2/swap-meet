#Wave 1

class Vendor:
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []
    '''
        if inventory is not None:
            self.inventory = inventory
        else:
            self.inventory = []
    '''
        
    def add(self,new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove        
        return None

    def get_by_id(self,id):
        if id is None:
            return None
        for item in self.inventory:
            if item.id == id:
                return item
        return None

# Wave 3
    def swap_items(self,other_vendor,my_item,their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

# Wave 4
    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self.swap_items(other_vendor,self.inventory[0],other_vendor.inventory[0])
        return True

# Wave 6
    def get_by_category(self,category):
        if not self.inventory:
            return []
        list_items_by_category = []
        
        for item in self.inventory:
            if item.get_category() == category:
                list_items_by_category.append(item)
        return list_items_by_category

    def get_best_by_category(self,category):
        list_of_items_in_category = self.get_by_category(category)
        if not list_of_items_in_category:
            return None
        best_item = max(list_of_items_in_category,key = lambda item: item.condition) 
        return best_item

    def swap_best_by_category(self,other_vendor,my_priority,their_priority):    
        best_item_from_my_inventory = self.get_best_by_category(their_priority)
        best_item_from_their_inventory = other_vendor.get_best_by_category(my_priority)
        if not best_item_from_my_inventory or not best_item_from_their_inventory:
            return False
        self.swap_items(other_vendor,best_item_from_my_inventory,best_item_from_their_inventory)
        return True

#Wave 7 
    def display_inventory(self,category = ""):
        if self.inventory == []: 
            print("No inventory to display.")
            return None
        
        if category:
            inventory_items_by_category = self.get_by_category(category)
            if inventory_items_by_category:
                for index in range(len(inventory_items_by_category)):
                    print(f"{index +1}. {inventory_items_by_category[index]}")
            else:
                print("No inventory to display.")
        else:
            for index in range(len(self.inventory)):
                    print(f"{index +1}. {self.inventory[index]}")

    def swap_by_id(self,other_vendor,my_item_id = None,their_item_id = None):
        my_item = self.get_by_id(my_item_id)
        vendor_item = other_vendor.get_by_id(their_item_id)
        if not my_item or not vendor_item:
            return False
        result = self.swap_items(other_vendor,my_item,vendor_item)
        return result

    def choose_and_swap_items(self,other_vendor,category = ""):
        if not category:
            self.display_inventory()
            other_vendor.display_inventory()
        else:
            self.display_inventory(category)
            other_vendor.display_inventory(category)
        my_item_id = int(input("Enter Id of the item you want to swap"))
        vendor_item_id = int(input("Enter Id of your friend vendor's item you want to swap with"))
        if not self.get_by_id(my_item_id) or not other_vendor.get_by_id(vendor_item_id):
            return False
        self.swap_by_id(other_vendor,my_item_id,vendor_item_id)
        return True

    
        
    

