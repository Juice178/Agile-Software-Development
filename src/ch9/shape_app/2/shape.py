from abc import ABC, abstractmethod
from pydantic import BaseModel

class Shape(BaseModel, ABC):
    @abstractmethod
    def draw(self) -> None:
        pass
