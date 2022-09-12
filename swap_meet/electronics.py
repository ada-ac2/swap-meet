from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, condition=0, type="Unknown") -> None:
        super().__init__(id, condition)
        self.type = type

    def __str__(self) -> str:
        base_desc = super().__str__()
        return f"{base_desc}. This is a {self.type} device."
