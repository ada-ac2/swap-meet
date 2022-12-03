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