import uuid

class Item:
    cond_descriptions = ["Poor",
                         "Heavily Used",
                         "Fair",
                         "Good"
                         "Very Good",
                         "Mint"]

    def __init__(self, id= None, condition=0) :
        if id is not None:
            if type(id) is int:
                self.id = id
            else:
                raise ValueError("The id for Item object must be an integer")
        else:
            self.id = uuid.uuid4().int

        self.condition = round(condition)

    def get_category(self):
        return self.__class__.__name__

    def __str__(self) -> str:
        str_item = f"An object of type {self.get_category()} with id {self.id}"
        return str_item

    def condition_description(self):
        return self.cond_descriptions[int(self.condition)]
