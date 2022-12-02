class Vendor:
    #constructor for vendor
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory is not None else []
    
    #function to add new item to inventory list. 
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    #function to remove a given item from inventory 
    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return None
        self.inventory.remove(item_to_remove)
        return item_to_remove
    
    #function to retreive item based on custom Id
    def get_by_id(self, id):

        for item in self.inventory:
            if item.id==id:
                return item
        return None
    
    #Making a method to swap items

    def swap_items(self, vendor_friend, item_to_give, item_to_get):

        #since the items are returned from their functions 
        #I can add and remove at the same time
        if item_to_give not in self.inventory or item_to_get not in vendor_friend.inventory:
            return False

        vendor_friend.add(self.remove(item_to_give))
        self.add(vendor_friend.remove(item_to_get))

        return True
    

    def swap_first_item(self, vendor_friend):
        
        if not self.inventory or not vendor_friend.inventory:
            return False
        return self.swap_items(vendor_friend, self.inventory[0], vendor_friend.inventory[0])
    
    #get items from inventory by catagory
    def get_by_category(self, category_string):

        return [item for item in self.inventory if item.get_category() == category_string]
        
    
    # getting best by for catagory 

    def get_best_by_category(self, category_string):
        if self.get_by_category(category_string):
            return max(self.get_by_category(category_string), key=lambda item: item.condition)
        return None

    #swap best by catagory
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not self.get_by_category(their_priority) or not other_vendor.get_by_category(my_priority):
            return False
        return self.swap_items(other_vendor, self.get_best_by_category(their_priority), other_vendor.get_best_by_category(my_priority))

    #create a function to display inventory. 
    def display_inventory(self, category = None):
        #create a list based on catagory or no
        inventory = self.get_by_category(category) if category else self.inventory
        if not inventory: 
            print  ("No inventory to display.")
        
        counter = 1
        for item in inventory:
            print (f"{counter}. " + str(item))
            counter += 1
    
    #swapping by id. 
    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        if not self.get_by_id(my_item_id) or not other_vendor.get_by_id(their_item_id):
            return False
        return self.swap_items(other_vendor,self.get_by_id(my_item_id),  other_vendor.get_by_id(their_item_id))

    #choose and swap items!
    def choose_and_swap_items(self, other_vendor, category = None):
        self.display_inventory(category)
        other_vendor.display_inventory(category)
        my_item_id = input("Please enter the id of the item from the first vendor to swap")
        their_item_id = input("Please input item of other vendor item you wish you swap")
        return self.swap_by_id(other_vendor, int(my_item_id), int(their_item_id))

