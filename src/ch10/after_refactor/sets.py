from typing import Generic, TypeVar, Any, Optional
from abc import ABC

from third_party.sets import BoundedSet as ThirdPartyBoundedSet
from third_party.sets import UnboundedSet as ThirdPartyUnboundedSet
from third_party.sets import PersistentSet as ThirdPersistentSet
from third_party.sets import PersistentObject

T = TypeVar('T')


class MemberContainer(ABC, Generic[T]):
    def __init__(self, container: Any):
        self._container = container
        self._size = len(container)
        self._pos = 0
    def __len__(self) -> int:
        return self._size
    def remove(self, element: T) -> None:
        self._container.remove(element)
    def is_in(self, element: T) -> bool:
        return element in self._container
    def __iter__(self):
        return self
    def __next__(self):
        if self._pos >= len(self._container):
            raise StopIteration
        val = list(self._container)[self._pos]
        self._pos += 1
        return val


class Set(MemberContainer, Generic[T]):
    def __init__(self, elements: list[T], size: Optional[int] = None):
        if size:
            super().__init__(ThirdPartyBoundedSet[T](elements, size))
        else:
            super().__init__(ThirdPartyUnboundedSet[T](ThirdPartyUnboundedSet(elements)))
    def add(self, element):
        self._container.add(element)


class PersistentSet(MemberContainer, Generic[T]):
    def __init__(self, elements: list[T]):
        super().__init__(ThirdPersistentSet[T](elements))
    def add(self, element: T):
        if not isinstance(element, PersistentObject):
            raise Exception("element is not PersistentObject")
        self._container.add(element)