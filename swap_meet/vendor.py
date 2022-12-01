class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory is None else inventory 
        print(self.inventory)
        if type(self.inventory) is not list:
            raise TypeError("Please enter the inventory as a list.")

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return None
        
        return item

# friend = Vendor()
# friend.remove("bracelet")
#print(friend.inventory)