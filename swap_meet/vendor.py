class Vendor:
    
    def __init__( self, inventory = None ):
        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory


    def add( self, item ):
        self.inventory.append( item )
        return item


    def remove( self, item ):
        if self.inventory == None or item not in self.inventory:
            return None
        
        self.inventory.remove( item )
        return item


    def get_by_id (self, item_id ):
        if not self.inventory:
            return None

        for item in self.inventory:
            if item.id == item_id:
                return item
        
        return None


    def swap_items( self, other_vendor, my_item, their_item ):        
        if not self.inventory or \
            not other_vendor.inventory or \
            not my_item or not their_item or \
            my_item not in self.inventory or \
            their_item not in other_vendor.inventory:
            return False

        self.add( their_item )
        other_vendor.add( my_item )         
        self.remove( my_item )
        other_vendor.remove( their_item )
        
        return True


    def swap_first_item( self, other_vendor ):
        if not self.inventory or \
        not other_vendor.inventory:
            return False

        return self.swap_items( other_vendor, self.inventory[0], other_vendor.inventory[0] )


    def get_by_category( self, category = None ):
        list_of_objects = []
        
        if not self.inventory or category == None:
            return []
        
        for item in self.inventory:
            if item.get_category() == str(category):
                list_of_objects.append( item )
        
        return list_of_objects


    def get_best_by_category( self, category ):        
        list_of_objects = self.get_by_category(category)
        
        if not list_of_objects:
            return None
        
        best_item = list_of_objects[0]
        for item in list_of_objects:
            if item.condition > best_item.condition:
                best_item = item

        return best_item


    def swap_best_by_category( self, other_vendor, my_priority, their_priority ):
        
        best_item_for_them = self.get_best_by_category(their_priority)
        best_item_for_me = other_vendor.get_best_by_category(my_priority)
        
        return self.swap_items(other_vendor, best_item_for_them, best_item_for_me)


    def display_inventory(self, category = None):
        if not self.inventory:
            print("No inventory to display.")
            return None
        
        if category == None:
            
            for index in range( len( self.inventory )):
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


    def swap_by_id( self, other_vendor, my_item_id, their_item_id ):
        my_item = self.get_by_id( my_item_id )
        their_item = other_vendor.get_by_id( their_item_id )
        
        if not my_item or not their_item:
            return False
        
        else:
            return self.swap_items(other_vendor, my_item, their_item)

    def choose_and_swap_items( self, other_vendor, category = None ):
        if category == None:
            self.category = ""
        else:
            self.category = category
        
        self.display_inventory( self.category )
        other_vendor.display_inventory( self.category )

        my_item_id = int( input( "Please enter the id of the item from my inventory:" )) 
        their_item_id = int( input( "Please enter the id of the item from their inventory:" ))

        if self.swap_by_id( other_vendor, my_item_id, their_item_id ):
            return True
        return False

# Function swap first two clothing with the same attribute fabric
# If we want to swap all clothing with the same fabric
# we can use next function : swap_all_clothing_by_attributes( self, other_vendor )
    def swap_clothing_by_attributes( self, other_vendor ):
        list_of_my_clothing = self.get_by_category( "Clothing" )
        list_of_their_clothing = other_vendor.get_by_category( "Clothing" )

        for my_item in list_of_my_clothing:
            for their_item in list_of_their_clothing:

                if my_item.fabric == their_item.fabric:
                    self.swap_by_id( other_vendor, my_item.id, their_item.id )
                    return True

        return False

# Function swap all clothing with the same attribute fabric
    def swap_all_clothing_by_attributes( self, other_vendor ):
        list_of_my_clothing = self.get_by_category( "Clothing" )
        list_of_their_clothing = other_vendor.get_by_category( "Clothing" )
        counter = 0

        for my_item in list_of_my_clothing:
            for their_item in list_of_their_clothing:
                
                if my_item.fabric == their_item.fabric:
                    counter +=1
                    self.swap_by_id( other_vendor, my_item.id, their_item.id )
        
        if counter > 0:
            return True

        return False


    def swap_decor_by_attributes( self, other_vendor ):
        list_of_my_decor = self.get_by_category( "Decor" )
        list_of_their_decor = other_vendor.get_by_category( "Decor" )

        for my_item in list_of_my_decor:
            for their_item in list_of_their_decor:
                
                if my_item.width == their_item.width \
                    and my_item.lenght == their_item.lenght \
                    or my_item.width * my_item.lenght == their_item.width * their_item.lenght:
                    self.swap_by_id( other_vendor, my_item.id, their_item.id )
                    return True

        return False
    
    def swap_electronics_by_attributes( self, other_vendor ):
        list_of_my_electronics = self.get_by_category( "Electronics" )
        list_of_their_electronics = other_vendor.get_by_category( "Electronics" )

        for my_item in list_of_my_electronics:
            for their_item in list_of_their_electronics:

                if my_item.type == their_item.type:
                    self.swap_by_id( other_vendor, my_item.id, their_item.id )
                    return True

        return False