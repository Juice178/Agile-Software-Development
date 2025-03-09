from abc import ABC


class Heater(ABC):
    _on = False
    @classmethod
    def engage(cls) -> None:
        pass
    @classmethod
    def disengage(cls) -> None:
        pass