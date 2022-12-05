import uuid

class Item:
    def __init__( self, id = None, ):
        if id == None:
            self.id = uuid.uuid1().int
        else:
            self.id = id

    def __str__(self):
        return f"An object of type Item with id {str(self.id)}"      

    def get_category( self ):
        category = self.__class__
        return str(category.__name__)
