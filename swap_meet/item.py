import uuid

class Item:

    def __init__( self, id = None, condition = None ):
        if id == None:
            self.id = uuid.uuid1().int
        else:
            self.id = id
        
        if condition == None:
            self.condition = 0
        elif condition > 5 or condition < 0:
            raise IndexError( "Please choose condition in range 0 - 5." )
        else:
            self.condition = condition


    def get_category( self ):
        return self.__class__.__name__


    def __str__( self ):
        return f"An object of type {self.get_category()} with id {str(self.id)}"

    
    def condition_description( self ):
        condition_list = ["Poor Condition",     # condition = 0
                        "Heavily Used",         # condition = 1
                        "Used - Good Condition",      # condition = 2
                        "Used - Very Good Condition", # condition = 3
                        "Used - Great Condition",   # condition = 4
                        "New"]                      # condition = 5
        return condition_list[self.condition]