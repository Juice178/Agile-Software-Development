from abc import ABC
import consts


class Thermometer(ABC):
    @classmethod
    def read(cls) -> float:
        print(f"TEMPERATURE IS: {consts.TEMPERATURE}")
        return consts.TEMPERATURE