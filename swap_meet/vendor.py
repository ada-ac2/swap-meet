from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

class Vendor:
    def __init__(self, inventory = None) :
        self.inventory = inventory if inventory is not None else []

    def add(self, item):
        if not item:
            return item

        if item not in self.inventory:
            self.inventory.append(item)
        
        return item

    def remove(self, item):  
        if not item:
            return item

        if item not in self.inventory:
            return None

        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item

        return None

    def get_by_category(self, category):
        if not category: 
            return []

        list_by_cate = [item for item in self.inventory if item.get_category() == category]
    
        return list_by_cate 

    def get_best_by_category(self, category):
        items_by_cate = self.get_by_category(category)

        if not items_by_cate:
            return None

        best_item = max(items_by_cate, key = lambda item: item.condition)
        return best_item

    def get_clothes_by_fabric(self,fabric):
        clothing = [item for item in self.inventory if isinstance(item, Clothing) 
                    and item.fabric == fabric]
        return clothing

    def get_decors_by_space(self, space):
        decors = [item for item in self.inventory if isinstance(item, Decor)
                  and item.get_space() == space]
        return decors

    def get_electronics_by_type(self, type):
        electronics = [item for item in self.inventory if isinstance(item, Electronics)
                       and item.type == type]
        return electronics

    def display_inventory(self, category=""):
        display_items = self.get_by_category(category) if category else self.inventory
        
        if not display_items:
            print("No inventory to display.")
            return

        for i in range(len(display_items)):
            print(f"{i+1}. {display_items[i]}")

    def swap_items(self, other_vendor, my_item, their_item):
        if other_vendor is None or my_item is None or their_item is None:
            return False

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        self.add(their_item)
        other_vendor.add(my_item)
        self.remove(my_item)
        other_vendor.remove(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        return self.swap_items(other_vendor,self.inventory[0],other_vendor.inventory[0])

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        if not my_priority or not their_priority:
            return False

        my_interest_item = other_vendor.get_best_by_category(my_priority)
        their_interest_item = self.get_best_by_category(their_priority)

        if not my_interest_item or not their_interest_item:
            return False

        return self.swap_items(other_vendor,their_interest_item,my_interest_item)

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        my_item = self.get_by_id(my_item_id)
        their_item = other_vendor.get_by_id(their_item_id)

        return self.swap_items(other_vendor,my_item,their_item)

    '''
    Swaps a Decor item between self and other_vendor by the space the items use
    - my_desired_space is a tuple that holds the lenght and width if the Decor item self would like to get
    - their_desired_space is tuple that holds the lenght and width of the Decor item other_vendor
       would like to get
    It goes throught both inventories and swaps the first items that match the desired areas returning True
    If there aren't items matching the spaces desired in the respective inventories 
    the swap doesn't happpen and returns False
    '''
    def swap_decor_by_space_used(self, other_vendor, my_desired_space, their_desired_space):
        if not other_vendor:
            return False

        my_items_with_their_space = self.get_decors_by_space(their_desired_space)
        if not my_items_with_their_space:
            return False

        their_items_with_my_space = other_vendor.get_decors_by_space(my_desired_space)
        if not their_items_with_my_space:
            return False

        '''
        Swaping occurs. Didn't used the function swap_items to avoid going through validations and looking 
        for the item twice'''
        self.add(their_items_with_my_space[0])
        other_vendor.add(my_items_with_their_space[0])
        self.remove(my_items_with_their_space[0])
        other_vendor.remove(their_items_with_my_space[0])

        return True

    def swap_clothing_by_fabric(self, other_vendor, fabric):
        if not other_vendor:
            return False

        my_items_with_fabric = self.get_clothes_by_fabric(fabric)
        if not my_items_with_fabric:
            return False

        their_items_with_fabric = other_vendor.get_clothes_by_fabric(fabric)
        if not their_items_with_fabric:
            return False

        '''
        Swaping occurs. Didn't used the function swap_items to avoid going through validations and looking 
        for the item twice'''
        self.add(their_items_with_fabric[0])
        other_vendor.add(my_items_with_fabric[0])
        self.remove(my_items_with_fabric[0])
        other_vendor.remove(their_items_with_fabric[0])

        return True

    def swap_electronics_by_type(self,other_vendor, type):
        if not other_vendor:
            return False

        my_electronics_type = self.get_electronics_by_type(type)
        if not my_electronics_type:
            return False

        their_electronics_type = other_vendor.get_electronics_by_type(type)
        if not their_electronics_type:
            return False

        '''
        Swaping of the first found occurs. Didn't used the function swap_items to avoid going through validations and looking 
        for the item twice'''
        self.add(their_electronics_type[0])
        other_vendor.add(my_electronics_type[0])
        self.remove(my_electronics_type[0])
        other_vendor.remove(their_electronics_type[0])

        return True

    def choose_and_swap_items(self, other_vendor, category=""):
        print("My items:")
        self.display_inventory(category)
        print("\nTheir items:")
        other_vendor.display_inventory(category)

        try:
            my_item_id = int(input("Provide the id of the item you want swap: "))
            their_item_id = int(input("Provide the id of the item they want to swap: "))

        except ValueError:
            print("An invalid id was provided")
            return False

        return self.swap_by_id(other_vendor,my_item_id,their_item_id)


