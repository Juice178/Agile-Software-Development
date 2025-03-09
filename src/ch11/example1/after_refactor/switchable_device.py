from abc import ABC, abstractmethod


class SwitchableDevice(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass
    @abstractmethod
    def turn_off(self) -> None:
        pass