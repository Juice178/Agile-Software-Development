import consts


class Thermometer:
    @classmethod
    def read(cls) -> float:
        print(f"TEMPERATURE IS: {consts.TEMPERATURE}")
        return consts.TEMPERATURE