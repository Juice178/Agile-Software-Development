from typing import TypeVar
from abc import ABC, abstractmethod

from third_party.sets import BoundedSet as ThirdPartyBoundedSet
from third_party.sets import UnboundedSet as ThirdPartyUnboundedSet

T = TypeVar('T')


class Set(ABC):
    @abstractmethod
    def add(self, element: T) -> None:
        pass
    @abstractmethod
    def delete(self, element: T) -> None:
        pass
    @abstractmethod
    def is_member(self, element: T) -> bool:
        pass


class UnboundedSet(Set):
    def __init__(self, elements: list[T]):
        self._container = ThirdPartyUnboundedSet(elements)
    def add(self, element):
        self._container.add(element)
    def delete(self, element):
        self._container.remove(element)
    def is_member(self, element):
        return element in self._container


class BoundedSet(Set):
    def __init__(self, elements: list[T], size: int):
        self._container = ThirdPartyBoundedSet(elements, size)
    def add(self, element):
        self._container.add(element)
    def delete(self, element):
        self._container.remove(element)
    def is_member(self, element):
        return element in self._container