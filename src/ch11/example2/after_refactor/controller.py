from io_channel_heater import Furnace
from io_channel_thermometer import Thermometer


def regulate(min_temp: float, max_temp: float) -> None:
    temperature: float = Thermometer.read()
    if temperature > min_temp and temperature < max_temp:
        return
    if temperature < min_temp:
        Furnace.engage()
    if temperature > max_temp:
        Furnace.disengage()
