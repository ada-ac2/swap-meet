import uuid
from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None,):
        if inventory is None:
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
    
    def swap_items(self, b_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in b_vendor.inventory :
            return False
        else:
            self.remove(my_item)
            b_vendor.add(my_item)
            self.add(their_item)
            b_vendor.remove(their_item)
            return True

    def swap_first_item(self,b_vendor):
        if  len(self.inventory) == 0 or len(b_vendor.inventory) == 0:
            return False
        else:
            my_item = self.inventory.pop(0)
            b_vendor.add(my_item)
            their_item = b_vendor.inventory.pop(0)
            self.add(their_item)
            return True

    def get_by_category(self, category):
        item_lst = []
        for item in self.inventory:
            if item.get_category() == category:
                item_lst.append(item)
        return item_lst
                
    #max()?
    def get_best_by_category(self, category):
        category_lst = self.get_by_category(category)
        if len(category_lst) == 0:
            return None
        else:
            n = sorted(category_lst, key=lambda item: item.condition, reverse= True)
        return n[0]

    def swap_best_by_category(self, other_vendor, my_priority,their_priority):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        their_want_item = self.get_best_by_category(their_priority)
        
        my_want_item = other_vendor.get_best_by_category(my_priority)
        #if not my_priority_item or not their_priority_item:
            #return "False2"
        n = self.swap_items(other_vendor, their_want_item, my_want_item)
        return n


        