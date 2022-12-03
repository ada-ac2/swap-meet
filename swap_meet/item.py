import uuid

class Item:
    #initalialize id to item
    def __init__(self,id = None):
        if id is not None:
            self.id = id
            print(id)
        else:
            self.id = uuid.uuid4().int
        

    def get_category(self):
        return self.__class__.__name__

    #stringify Item and return str
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"