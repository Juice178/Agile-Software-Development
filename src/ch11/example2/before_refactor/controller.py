from furnace import Furnace
from thermometer import Thermometer


def regulate(min_temp: float, max_temp: float) -> None:
    temperature: float = Thermometer.read()
    if temperature > min_temp and temperature < max_temp:
        return
    if temperature < min_temp:
        Furnace.engage()
    if temperature > max_temp:
        Furnace.disengage()
