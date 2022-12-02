import uuid

class Item:
    def __init__(self, id = None, condition = 0):
        if not id:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        self.condition = condition
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"
        
    def condition_description(self):
        #condition scale 0-5
        if self.condition == 0:
            return "Yikes!"
        elif 0 < self.condition <= 1:
            return "Bad"
        elif 1 < self.condition <= 2:
            return "Poor"
        elif 2 < self.condition <= 3:
            return "Fair"
        elif 3 < self.condition <= 4:
            return "Good"
        elif 4 < self.condition <= 5:
            return "Excellent"
