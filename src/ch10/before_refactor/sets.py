from typing import Generic, TypeVar, Any
from abc import ABC, abstractmethod

from third_party.sets import BoundedSet as ThirdPartyBoundedSet
from third_party.sets import UnboundedSet as ThirdPartyUnboundedSet
from third_party.sets import PersistentSet as ThirdPersistentSet
from third_party.sets import PersistentObject

T = TypeVar('T')


class Set(ABC, Generic[T]):
    def __init__(self, container: Any):
        self._container = container
        self._size = len(container)
        self._pos = 0
    def __len__(self) -> int:
        return self._size
    @abstractmethod
    def add(self, element: T) -> None:
        pass
    @abstractmethod
    def delete(self, element: T) -> None:
        pass
    @abstractmethod
    def is_member(self, element: T) -> bool:
        pass
    def __iter__(self):
        return self
    def __next__(self):
        if self._pos >= len(self._container):
            raise StopIteration
        val = list(self._container)[self._pos]
        self._pos += 1
        return val


class UnboundedSet(Set, Generic[T]):
    def __init__(self, elements: list[T]):
        super().__init__(ThirdPartyUnboundedSet[T](ThirdPartyUnboundedSet(elements)))
        # self._container = ThirdPartyUnboundedSet(elements)
    def add(self, element):
        self._container.add(element)
    def delete(self, element):
        self._container.remove(element)
    def is_member(self, element):
        return element in self._container


class BoundedSet(Set, Generic[T]):
    def __init__(self, elements: list[T], size: int):
        super().__init__(ThirdPartyBoundedSet[T](elements, size))
        # self._container = ThirdPartyBoundedSet(elements, size)
    def add(self, element: T):
        self._container.add(element)
    def delete(self, element: T):
        self._container.remove(element)
    def is_member(self, element: T):
        return element in self._container
    

class PersistentSet(Set):
    def __init__(self, elements: list[T]):
        super().__init__(ThirdPersistentSet[T](elements))
    def add(self, element: T):
        if not isinstance(element, PersistentObject):
            raise Exception("element is not PersistentObject")
        self._container.add(element)
    def delete(self, element: T):
        self._container.remove(element)
    def is_member(self, element: T):
        return element in self._container