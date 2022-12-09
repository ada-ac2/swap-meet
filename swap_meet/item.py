import uuid

class Item:
    #initalialize id to item
    def __init__(self,id = None,condition = 0):
            if id is not None:
                #print(type(id))
                if type(id) != int:
                    raise TypeError("id needs to be an integer.")
                else:
                    self.id = id
                #print(id)
            else:
                self.id = uuid.uuid4().int
            self.condition = condition


    def get_category(self):
        return self.__class__.__name__

    #stringify Item and return str
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    #condiciton instance
    def condition_description(self):
        if self.condition > 4:
            return "Good condition!"
        elif self.condition > 2:
            return "It's still workable."
        else:
            return "Heavily used!"

    #get similar items
    #abstract method. refercence:https://www.geeksforgeeks.org/abstract-classes-in-python/
    def compare_item(self,other_item):
        pass