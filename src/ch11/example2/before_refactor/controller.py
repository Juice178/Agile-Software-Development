from time import sleep
import consts
from furnace import Furnace


def regulate(min_temp: float, max_temp: float) -> None:
    if consts.TEMPERATURE > min_temp and consts.TEMPERATURE < max_temp:
        return
    if consts.TEMPERATURE < min_temp:
        Furnace.engage()
    if consts.TEMPERATURE > max_temp:
        Furnace.disengage()
