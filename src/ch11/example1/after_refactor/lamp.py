from switchable_device import SwitchableDevice


class Lamp(SwitchableDevice):
    @classmethod
    def turn_on(cls) -> None:
        print("Turn on lamp")
        print("⭐⭐⭐⭐⭐⭐")
    @classmethod
    def turn_off(cls) -> None:
        print("Turn off lamp")
        print("📴📴📴📴📴📴")