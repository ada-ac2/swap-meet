class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return None
        self.inventory.remove(item)
        return item

    def get_by_id(self, id): #if id is None? ==> wave02
        for item in self.inventory:
            if item.id == id:            
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False        
        other_vendor.add(my_item)
        self.remove(my_item)     
        self.add(their_item)
        other_vendor.remove(their_item)    
        return True
    
    def swap_first_item(self, other_vendor):
        if not other_vendor.inventory or not self.inventory:
            return False
        first_my_item = self.remove(self.inventory[0])
        other_vendor.add(first_my_item)
        first_their_item = other_vendor.remove(other_vendor.inventory[0])
        self.add(first_their_item)
        return True

    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.get_category() == category:
                items.append(item)
        return items

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        best_condition = 0.0  
        best_item = None
        for item in items:
            if item.condition > best_condition:
                best_item = item
                best_condition = item.condition
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other_vendor.get_best_by_category(my_priority)

        return self.swap_items(other_vendor, my_item, their_item)
    
    #wave 07
    def display_inventory(self, category=""):
        display_items = self.get_by_category(category)
        if not self.inventory:
            print("No inventory to display.")
        elif not category:
            for i, item in enumerate(self.inventory):
                    print(f"{i+1}. {str(item)}")
        else:
            display_items = self.get_by_category(category)
            if not display_items:
                print("No inventory to display.")
            else:
                for i, item in enumerate(display_items):
                    print(f"{i+1}. {str(item)}")

    def swap_by_id(self, other_vendor, my_item_id,their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)

        return self.swap_items(other_vendor, my_item, their_item)
    
    def choose_and_swap_items(self, other_vendor, category=""):

        self.display_inventory(category)
        my_item_id = int(input("Enter an item id from your inventory: "))

        other_vendor.display_inventory(category)
        their_item_id = int(input("Enter an item id from your friend's inventory:  "))
        
        return self.swap_by_id(other_vendor, my_item_id, their_item_id)
        






