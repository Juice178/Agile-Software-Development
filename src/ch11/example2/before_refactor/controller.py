from furnace import Furnace
from thermometer import Thermometer


def regulate(min_temp: float, max_temp: float) -> None:
    temperature: float = Thermometer.read()
    if _is_comfortable():
        print("Comfortable temperature.")
        return
    if _is_too_cold():
        Furnace.engage()
    if _is_too_hot():
        Furnace.disengage()

    def _is_comfortable() -> bool:
        return temperature > min_temp and temperature < max_temp
    
    def _is_too_cold() -> bool:
        return temperature < min_temp
    
    def _is_too_hot() -> bool:
        return temperature > max_temp