from controller import regulate
import consts
from typing import Final
from time import sleep

from random import uniform

MIN_TEMP_IN_CELSIUS: Final[float] = 6.0
MAX_TEMP_IN_CELSIUS: Final[float] = 18.0


def main() -> None:
    while True:
        consts.TEMPERATURE = uniform(-10.0, 30)
        regulate(MIN_TEMP_IN_CELSIUS, MAX_TEMP_IN_CELSIUS)
        sleep(10)


if __name__ == "__main__":
    main()