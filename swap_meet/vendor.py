class Vendor:
    def __init__(self, inventory = None):
        self.inventory = [] if inventory == None else inventory 

    def add(self, item):
        self.inventory.append(item)
        return item


# friend = Vendor(["pj", "pc"])
# friend.add("bracelet")
# print(friend.inventory)