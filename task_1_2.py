class Technic:
    __slots__ = ('name', 'price', 'availability', 'category')

    def __init__(self, name:str, price:int, availability: bool):
        self.name = name
        self.price = price
        self.availability = availability

        if self.price > 100:
            self.category = 'expensive'
        else:
            self.category = 'cheap'

    def __eq__(self, other: object) -> bool:
        if len(other.name) == len(self.name):
            return True
        return False


tv = Technic('TV', 12, True)
tv2 = Technic('T2', 12, True)
if tv == tv2:
    print("Yess")