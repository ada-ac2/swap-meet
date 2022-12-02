class Vendor:
    
    def __init__(self, inventory=None):
        # Inventory attribute should be optional. 
        # If there is no inventory argument was passed into. The default value of inventory will be an empty list.
        self.inventory = inventory if inventory else []

