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

#this function will return True if swap successfully
#else, return False 
    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor,my_best_item,their_best_item)

#print out a string that has all the item in the inventory.
    def display_inventory(self,category = ""):
        index = 1
        if len(self.inventory) == 0:
            print("No inventory to display.")
        else:
            if category == "":
                for item in self.inventory:
                    print(str(index) + ". " + item.__str__())
                    index += 1
            else:
                for item in self.inventory:
                    if item.get_category()==category:
                        print(str(index) + ". " + item.__str__())
                        index += 1
                if index == 1:
                    print("No inventory to display.")

#swap items based on id
    def swap_by_id(self,other_vendor,my_item_id,their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)
        return self.swap_items(other_vendor,my_item,their_item)

#user pick items to swap by id
    def choose_and_swap_items(self,other_vendor,category = ""):
        self.display_inventory(category)
        other_vendor.display_inventory(category)
        my_item_id = int(input("Which item would you like to swap from my list?"))
        their_item_id = int(input("Which item would you like to swap from their list?"))
        return self.swap_by_id(other_vendor,my_item_id,their_item_id)


#swap similar item in each category
#assumption item to swap is from other vendor
#get category of the item user trying to swap
#iterate list of that category
#find similar material/size items and swap it
    def swap_similiar_material_items(self,other_vendor, item_to_swap = ""):
        if item_to_swap is None or len(self.inventory) == 0:
            return False
            print("No item to swap. Please enter item that you'd like to swap!")
        else:
            item_list = self.get_by_category(item_to_swap.get_category())
            for item in item_list:
                if Item.compare_item(item,item_to_swap) == True:
                    return self.swap_items(other_vendor,item,item_to_swap)
                else:
                    return self.swap_items(other_vendor,item,item_to_swap)
                    print (f"No similiar item in the {item_to_swap.get_category} category. Please try another item.")
            