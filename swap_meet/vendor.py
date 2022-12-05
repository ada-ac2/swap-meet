from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory = None):
        if inventory is not None:
            self.inventory = inventory
        else:
            self.inventory = []

#add new item and return inventory list
    def add(self,add_item):
        self.inventory.append(add_item)
        return add_item

#remove duplicates from inventory list if any, else return None
    def remove(self,check_item):
        if check_item in self.inventory:
            self.inventory.remove(check_item)
            return check_item
        else:
            return None

#check id in inventory,return id. if not, return None
    def get_by_id(self,id):
        for item in self.inventory:
            if id == item.id:
                return item
        else:
            return None

#swap item between vendors
    def swap_items(self,other_vendor,my_item,their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            other_vendor.inventory.remove(their_item)
            other_vendor.inventory.append(my_item)
            return True
            
        else:
            return False

#swap first item method takes one argument
# return True when successfully swap item.
# return False if any empty inventory list
    def swap_first_item(self,other_vendor):
        if len(self.inventory) == 0  or len(other_vendor.inventory) == 0:
            return False
        else:
            vendor_first_item = other_vendor.inventory[0]
            self_first_item = self.inventory[0]
            self.inventory[0] = vendor_first_item
            other_vendor.inventory[0] = self_first_item
            #another way to meet requirements.
            #self.inventory.remove(self_first_item)
            #self.inventory.append(vendor_first_item)
            #other_vendor.inventory.remove(vendor_first_item)
            #other_vendor.inventory.append(self_first_item)
            return True

#takes one str and return list of objefcts
#if no item in the list, return empty list
    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if item.get_category() == category:
                items_list.append(item)
        return items_list

#use sort(reverse = True) to sort the list
#return first item in the sorted list
    def get_best_by_category(self,category):
        item_list = self.get_by_category(category)
        best_item = None
        temp = 0
        for item in item_list:
            if item.condition > temp:
                temp = item.condition
                best_item = item
        return best_item


    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor,my_best_item,their_best_item)
