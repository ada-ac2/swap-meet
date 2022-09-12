from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0) -> None:
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def __str__(self) -> str:
        base_desc = super().__str__()
        return (
            f"{base_desc}. "
            f"It takes up a {self.width} by {self.length} sized space."
        )