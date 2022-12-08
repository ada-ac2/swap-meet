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
        their_priority_item = self.get_best_by_category(their_priority)
        my_priority_item = other_vendor.get_best_by_category(my_priority)

        if not other_vendor.get_by_category(my_priority) or not self.get_by_category(their_priority):
            return False
        
        self.remove(their_priority_item)
        other_vendor.remove(my_priority_item)   
        self.add(my_priority_item)         
        other_vendor.add(their_priority_item)
        return True

