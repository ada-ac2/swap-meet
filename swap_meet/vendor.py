from .item import Item
class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            inventory = []
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
    def get_by_id(self,id):
        for item in self.inventory:
            if item.id  == id:
                return item
        return 
 
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        else:
            return False
    def swap_first_item(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            first_item = self.inventory.pop(0)
            self.inventory.append(other_vendor.inventory[0])
            other_vendor.inventory.pop(0)
            other_vendor.inventory.append(first_item)
            return True
        else:
            return False
    
    def get_by_category(self, category):
        li = []
        for item in self.inventory:
            if type(item).__name__ == category:
                li.append(item)
        return li

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if category_list:
            curr_best_item = category_list[0]
            for item in category_list:
                if item.condition > curr_best_item.condition:
                    curr_best_item = item
            return curr_best_item

        else:
            return None
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        their_best_item =other_vendor.get_best_by_category(my_priority)
        my_best_item = self.get_best_by_category(their_priority)
        if not my_best_item or not their_best_item:
            return False
        else:
            return self.swap_items(other_vendor, my_best_item, their_best_item)

    def display_inventory(self, category =""):
        if category:
            category_list = self.get_by_category(category)
            if category_list:
                for num, item in enumerate(category_list,1):
                    print(f"{num}. " + str(item))
            else:
                print("No inventory to display.")
                
        else:
            inventory_list =  self.inventory
            if inventory_list:
                for num, item in enumerate(inventory_list,1):
                    print(f"{num}. " + str(item))
            else: 
                print("No inventory to display.")

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_dic = {}
        their_dic = {}
        for item in self.inventory:
            my_dic[item.id] = item
        for item in other_vendor.inventory:
            their_dic[item.id] = item

        if my_item_id in my_dic and their_item_id in their_dic:
            self.inventory.remove(my_dic[my_item_id])
            other_vendor.inventory.append(my_dic[my_item_id])
            other_vendor.inventory.remove(their_dic[their_item_id])
            self.inventory.append(their_dic[their_item_id])
            return True
        else:
            return False

    def choose_and_swap_items(self, other_vendor, category=""):
    
        self.display_inventory(category)
        other_vendor.display_inventory(category)
        user_input_1 = input(f"Please provide the id of an item from your inventory list you want to swap: \n")
        my_item_id = int(user_input_1)
        user_input_2 = input(f"Please provide the id of an item from your friend's inventory list you want to receive \n")
        their_item_id = int(user_input_2)

        return self.swap_by_id(other_vendor, my_item_id, their_item_id)



