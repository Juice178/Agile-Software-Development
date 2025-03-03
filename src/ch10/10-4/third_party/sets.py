class UnboundedSet(set):
    pass


class BoundedSet(set):
    def __init__(self, elements: list, n: int) -> None:
        super().__init__(elements)
        self._size = len(elements) if len(elements) > n else n
    def size(self):
        return self._size
    def add(self, element):
        if len(self) < self.size():
            super().add(element)


ul = UnboundedSet([2,3])
print(ul, len(ul))

bl = BoundedSet([2,3], 2)
bl.add(6)
print(bl, len(bl))