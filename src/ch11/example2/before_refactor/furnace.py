class Furnace:
    _on = False
    @classmethod
    def engage(cls) -> None:
        if not cls._on:
            print("Turn on device")
            cls._on = True
        else:
            print("Already turned on")

    @classmethod
    def disengage(cls) -> None:
        if cls._on:
            print("Turn off device")
            cls._on = False
        else:
            print("Already turned off")