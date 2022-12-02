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

