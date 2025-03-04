from typing import Generic, TypeVar


T = TypeVar('T')

class UnboundedSet(set, Generic[T]):
    def __init__(self, elements: list[T]) -> None:
        super().__init__(elements)


class BoundedSet(set, Generic[T]):
    def __init__(self, elements: list[T], n: int) -> None:
        super().__init__(elements)
        self._size = len(elements) if len(elements) > n else n
    def size(self):
        return self._size
    def add(self, element):
        if len(self) < self.size():
            super().add(element)


class PersistentObject:
    pass


class PersistentSet(set):
    def __init__(self, elements: list[PersistentObject]) -> None:
        super().__init__(elements)
    def size(self):
        return self._size
    def add(self, element: PersistentObject):
        super().add(element)


# ul = UnboundedSet([2,3])
# print(ul, len(ul))

# bl = BoundedSet([2,3], 2)
# bl.add(6)
# print(bl, len(bl))