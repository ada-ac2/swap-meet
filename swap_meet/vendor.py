class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory if inventory else [] 
    
    def add(self, item): 
        # Check input validation 
        item = item.strip() 
        if not item: 
            raise ValueError("Invalid Input")
        # Check duplicated item 
        if item in self.inventory: 
            raise ValueError("Item already exist in the current inventory, item has not been added")

        self.inventory.append(item) 

        return item 

    def remove(self, item): 
        if item not in self.inventory: 
            return None 
            
        self.inventory.remove(item)
        return item 

    def get_by_id(self, item_id): 
        for item in self.inventory: 
            if item.id == item_id:
                return item
        return None # Return None if no matching item 
