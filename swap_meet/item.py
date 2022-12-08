import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid1().int if not id else id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}"

    def condition_description(self):
        descriptions = {0: "torn", 1: "a bit shredded", 2: "defs used", 3: "lightly used", 4: "near perfect", 5: "perf",}
        return descriptions[self.condition]
