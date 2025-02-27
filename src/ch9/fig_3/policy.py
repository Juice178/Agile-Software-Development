from abc import ABC, abstractmethod


class Policy(ABC):
    def __init__(self, name: str):
        self._name = name
    def policy_function(self) -> None:
        print(f"Start policy {self._name}")
        res = self._service_function()
        print(f"Policy Result = {res}")
        print(f"End policy {self._name}")

    @abstractmethod
    def _service_function(self) -> None:
        pass


class AddPolicy(Policy):
    def __init__(self,num_1: int, num_2: int):
        super().__init__("Add")
        self._num_1 = num_1
        self._num_2 = num_2
    def _service_function(self) -> int:
        return self._num_1 + self._num_2


class SubtractPolicy(Policy):
    def __init__(self, num_1: int, num_2: int):
        super().__init__("Subtract")
        self._num_1 = num_1
        self._num_2 = num_2
    def _service_function(self) -> int:
        return self._num_1 - self._num_2