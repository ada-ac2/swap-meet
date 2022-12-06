class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory else []

    def add(self, item):
        """
        Adds item to Vendor.inventory
        :params:    (obj) item: item to add
        :returns:   (obj) item added
        """
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        """
        Remove item to Vendor.inventory
        :params:    (obj) item: to remove
        :returns:   (obj) item removed or None
        """
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return None
    
    def get_by_id(self, id):
        """
        Retrieves item by id
        :params:    (int) id: id of item
        :returns:   (obj) item with id or None

        """
        result = list(filter(lambda item: item.id == id, self.inventory))
        return result[0] if result else None
    
    def swap_items(self, other_vendor, my_item, their_item):
        """
        Swaps two indicated items between vendors
        :params:    (obj) other_vendor: other vendor to switch with
                    (obj) my_item: my item to switch
                    (obj) their_item: other vendor's item to switch
        :returns:   (bool) True if items swapped or False
        """
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            other_vendor.add(my_item)
            other_vendor.remove(their_item)
            return True
            
    def swap_first_item(self, other_vendor):
        """
        Swaps first position items in inventory between vendors
        :params:    (obj) other_vendor: other vendor to switch with
        :returns:   (bool) True if items swapped or False
        """
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
            return True
        
    def get_by_category(self, category):
        """
        Retrieves items by inidicated category
        :params:    (str) category: category of items to get
        :returns:   (list) result: list of items from category indicated
        """
        result = list(
            filter(lambda item: item.get_category() == category, self.inventory)
        )
        return result
    
    def get_best_by_category(self, category=None, list=None):
        """
        Retrieves best condition item in an indicated category or in a given list
        :params:    (str) category: category of items to select best of, default=None
                    (list) list: list of items to select best of, default=None
        :returns:   (obj) result: item in best condition or None
        """
        items = list if list else self.get_by_category(category)
        if items:
            result = max(items, key=lambda item: item.condition)
            return result
        return None

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """
        Swaps best condition item between vendors from an indicated category
        :params:    (obj) other_vendor: other vendor to switch with
                    (str) my_priority: category of item I want
                    (str) their_priority: category of item other vendor wants
        :returns:   (bool) True if swapped or False
        """
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)
        if not my_best or not their_best:
            return False
        else:
            self.swap_items(other_vendor, my_best, their_best)
            return True
        
    def display_inventory(self, category=''):
        """
        Prints items in inventory for a given category or all inventory if no category given
        :params:    (str) category: category of items to display
        """
        items = self.get_by_category(category) if category else self.inventory
        if items:
            [print(f'{i}. {item}') for i, item in enumerate(items, 1)]
        else:
            print('No inventory to display.')

    def swap_by_id(self, other_vendor, my_item_id, their_item_id):
        """
        Swaps items by id between two vendors
        :params:    (obj) other_vendor: other vendor to swap items with
                    (int) my_item_id: id of my item
                    (int) their_item_id: id of their item
        """
        my_item = self.get_by_id(my_item_id) 
        their_item = other_vendor.get_by_id(their_item_id)
        if not my_item or not their_item:
            return False
        else:
            self.swap_items(other_vendor, my_item, their_item)
            return True

    def choose_and_swap_items(self, other_vendor, category=''):
        """
        Displays inventory by category (or full inventory), prompts user for id selection of items to swap, and swaps items by ids
        :params:    (obj) other_vendor: other vendor to switch items with
                    (str) category: category of items to display for selection, default=''
        :returns:   (bool) True if swapped or False
        """
        [vendor.display_inventory(category) for vendor in [self, other_vendor]]
        temp_prompt = 'Please input the item ID you would like to '
        my_item_id = int(input(f'{temp_prompt} give other vendor: '))
        their_item_id = int(input(f'{temp_prompt} receive from other vendor: '))
        if self.swap_by_id(other_vendor, my_item_id, their_item_id):
            return True
        else:
            return False

    def get_by_category_attribute(self, category, attr, val):
        """
        Retrieves items by indicated category and attribute value
        :params:    (str) category: category of items to get
                    (str) attr: attribute of items to get
                    (int/str) val: value of attribute to select by
        :returns:   (list) items_by_attr: category items selected by attribute of equivalent value
        """
        items_by_attr = []
        items = self.get_by_category(category)
        for item in items:
            if val == getattr(item, attr):
                items_by_attr.append(item)
        return items_by_attr
    
    def swap_by_category_attribute(self, other_vendor, category, attr, attr_val):
        """
        Swaps items by indicated category and attribute value between two vendors
        :params:    (obj) other_vendor: other vendor to swap items with
                    (str) category: category of items to swap
                    (str) attr: attribute of items to swap
                    (str/int) attr_val: attribute value of items to select by
        :returns:   (bool) result: True if swapped or False
        """
        my_items = self.get_by_category_attribute(category, attr, attr_val)
        their_items = other_vendor.get_by_category_attribute(category, attr, attr_val)
        result = self.swap_items(
            other_vendor,
            self.get_best_by_category(list=my_items),
            other_vendor.get_best_by_category(list=their_items)
        )
        return result
