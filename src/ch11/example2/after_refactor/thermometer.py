from abc import ABC

class Thermometer(ABC):
    @classmethod
    def read(cls) -> float:
        pass