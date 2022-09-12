from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric="Unknown") -> None:
        super().__init__(id, condition)
        self.fabric = fabric

    def __str__(self) -> str:
        base_desc = super().__str__()
        return f"{base_desc}. It is made from {self.fabric} fabric."