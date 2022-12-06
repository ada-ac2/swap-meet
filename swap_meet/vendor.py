class Vendor:
    def __init__( self, inventory = None):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add( self, item):
        self.inventory.append(item)
        return item

    def remove( self, item):
        if self.inventory == None or item not in self.inventory:
            return None
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, item_id):
        if not self.inventory:
            return None

        for item in self.inventory:
            if item.id == item_id:
                return item
        
        return None

    def swap_items(self, other_vendor, my_item, their_item):        
        if not self.inventory or \
            not other_vendor.inventory or \
            not my_item or not their_item or \
            my_item not in self.inventory or \
            their_item not in other_vendor.inventory:
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item( self, other_vendor):
        if not self.inventory or \
        not other_vendor.inventory:
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

    def get_by_category(self, category):
        list_of_objects = []
        if not self.inventory:
            return []
        for index_item in range(len(self.inventory)-1):
            if self.inventory[index_item].get_category() == category:
                list_of_objects.append(self.inventory[index_item])
        return list_of_objects

    def get_best_by_category(self, category):        
        list_of_objects = self.get_by_category(category)
        if not list_of_objects:
            return None
        best_item = list_of_objects[0]
        for item in list_of_objects:
            if item.condition > best_item.condition:
                best_item = item
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        best_item_for_them = self.get_best_by_category(their_priority)
        best_item_for_me = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, best_item_for_them, best_item_for_me)

    def display_inventory(self, category = None):
        if not self.inventory:
            print("No inventory to display.")
            return None
        if category == None:
            for index in range(len(self.inventory)):
                print(f"{index+1}. {self.inventory[index]}")
        else:
            count = 0
            for item in self.inventory:
                if item.get_category() == category:
                    count += 1
                    print(f"{count}. {item}")
            if count == 0:
                print("No inventory to display.")
                return None   

    def swap_by_id( self, other_vendor, my_item_id, their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)
        if not my_item or not their_item:
            return False
        else:
            return self.swap_items(other_vendor, my_item, their_item)

    def choose_and_swap_items(self, other_vendor, category = None):
        if category == None:
            self.category = ""
        else:
            self.category = category
        self.display_inventory(self.category)
        other_vendor.display_inventory(self.category)

        my_item_id = int(input("Please enter the id of the item from my inventory:")) 
        their_item_id = int(input("Please enter the id of the item from their inventory:"))

        if self.swap_by_id(other_vendor, my_item_id, their_item_id):
            return True
        return False
        