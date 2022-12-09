import uuid
from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None):
        # inventory default []
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        
    #help function to check inventory empty
    def check_inventory_empty(self):
        if len(self.inventory) == 0:
            return None
    
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
    
    def swap_items(self, b_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in b_vendor.inventory :
            return False
        else:
            self.remove(my_item)
            b_vendor.add(my_item)
            self.add(their_item)
            b_vendor.remove(their_item)
            return True

    def swap_first_item(self,other_vendor):
        if self.check_inventory_empty() or other_vendor.check_inventory_empty():
            return False
        else:
            my_item = self.inventory.pop(0)
            other_vendor.add(my_item)
            their_item = other_vendor.inventory.pop(0)
            self.add(their_item)
            return True
    # List comprehension
    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]
                
    
    def get_best_by_category(self, category):
        category_lst = self.get_by_category(category)
        if len(category_lst) == 0:
            return None
        else:
            return max(category_lst, key=lambda item: item.condition)
        

    def swap_best_by_category(self, other_vendor, my_priority,their_priority):
        if self.check_inventory_empty() or other_vendor.check_inventory_empty():
            return False
        
        their_want_item = self.get_best_by_category(their_priority)
        
        my_want_item = other_vendor.get_best_by_category(my_priority)
        
        result = self.swap_items(other_vendor, their_want_item, my_want_item)
        return result

    def display_inventory(self, category=None):
        if self.check_inventory_empty():
        #if len(self.inventory) == 0:
            print("No inventory to display.")
        else:   
            if not category:
                for i in range(len(self.inventory)):
                    print(f"{i+1}. {self.inventory[i].__str__()}")
            
            else:
                item_lst = self.get_by_category(category)
                if len(item_lst)==0:
                    print("No inventory to display.")
                else:
                    for i in range(len(item_lst)):
                        print(f"{i+1}. {item_lst[i].__str__()}")

        

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)
        if  my_item and their_item:
            self.swap_items(other_vendor, my_item, their_item)
            return True
        return False
        
    def choose_and_swap_items(self, other_vendor, category=None):
        if not category:
            self.display_inventory()
            other_vendor.display_inventory()
        else:
            self.display_inventory(category)
            other_vendor.display_inventory(category)
        
        
        first_item = int(input("Please input a number"))
        second_item = int(input("Please input a number"))
        res = self.swap_by_id(other_vendor,first_item,second_item)
        return res

# new method swap clothing by fabric
    def swap_clothing_by_fabric(self, other_vendor, category, fabric):
        if self.check_inventory_empty() or other_vendor.check_inventory_empty():
            return False
        self_category_lst = self.get_by_category(category)
        other_category_lst = other_vendor.get_by_category(category)
        if len(self_category_lst) == 0 or len(other_category_lst) == 0:
            return False
        
        else:
            self_not_match_fabric = []
            for item_a in self_category_lst:
                if item_a.fabric == fabric:
                    their_want_item = item_a
                    break
                else:
                    self_not_match_fabric.append(item_a)
            if len(self_not_match_fabric) == len(self_category_lst):
              return False
        
            other_not_match_fabric = []       
            for item_b in other_category_lst:
                if item_b.fabric == fabric:
                    my_want_item = item_b
                    break
                else:
                   other_not_match_fabric.append(item_b)
            if len(other_not_match_fabric) == len(other_category_lst):
              return False
            result = self.swap_items(other_vendor, their_want_item, my_want_item)
            return result     


# new method swap electronics by type
    def swap_electronics_by_type(self, other_vendor, category, type):
        if self.check_inventory_empty() or other_vendor.check_inventory_empty():
            return False
        self_category_lst = self.get_by_category(category)
        other_category_lst = other_vendor.get_by_category(category)
        if len(self_category_lst) == 0 or len(other_category_lst) == 0:
            return False
        
        else:
            self_not_match_type = []
            for item_a in self_category_lst:
                if item_a.type == type:
                    their_want_item = item_a
                    break
                else:
                    self_not_match_type.append(item_a)
            if len(self_not_match_type) == len(self_category_lst):
              return False
        
            other_not_match_type = []       
            for item_b in other_category_lst:
                if item_b.type == type:
                    my_want_item = item_b
                    break
                else:
                   other_not_match_type.append(item_b)
            if len(other_not_match_type) == len(other_category_lst):
              return False
            result = self.swap_items(other_vendor, their_want_item, my_want_item)
            return result

# new method swap decor by space
    def swap_decor_by_space(self, other_vendor, category, space):
        if self.check_inventory_empty() or other_vendor.check_inventory_empty():
            return False
        self_category_lst = self.get_by_category(category)
        other_category_lst = other_vendor.get_by_category(category)
        if len(self_category_lst) == 0 or len(other_category_lst) == 0:
            return False
        
        else:
            self_not_match_space = []
            for item_a in self_category_lst:
                if item_a.space == space:
                    their_want_item = item_a
                    break
                else:
                    self_not_match_space.append(item_a)
            if len(self_not_match_space) == len(self_category_lst):
              return False
        
            other_not_match_space = []       
            for item_b in other_category_lst:
                if item_b.space == space:
                    my_want_item = item_b
                    break
                else:
                   other_not_match_space.append(item_b)
            if len(other_not_match_space) == len(other_category_lst):
              return False
            result = self.swap_items(other_vendor, their_want_item, my_want_item)
            return result