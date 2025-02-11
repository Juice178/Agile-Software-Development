from abc import ABC, abstractmethod

class ClientInterface(ABC):
    @abstractmethod
    def echo(self, string: str) -> None:
        pass
