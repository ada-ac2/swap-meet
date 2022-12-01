class Vendor:
    def __init__(self, inventory = None):
        #validate that iventory is a list
        self.inventory = [] if inventory == None else inventory 

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return None
        
        return item

# friend = Vendor(["pj", "pc"])
# friend.remove("bracelet")
# print(friend.inventory)