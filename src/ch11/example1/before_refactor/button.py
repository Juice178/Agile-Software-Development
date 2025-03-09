from lamp import Lamp
from threading import Thread, Lock
from time import sleep


class Button(Thread):
    _its_lamp: Lamp = Lamp
    def __init__(self) -> None:
        super().__init__(name='button', daemon=True)
        self.running = False
        self._pushed = False
        self._state = 'off'
    
    def run(self) -> None:
        self.running = True
        self.work()

    def work(self) -> None:
        while self.running:
            self.poll()

    def push(self) -> None:
        print("pushed")
        self._pushed = True
        if self._state == 'on':
            self._state = 'off'
        else:
            self._state = 'on'

    def poll(self) -> None:
        while True:
            print("Polling state")
            if self._pushed and self._state == 'on':
                self._its_lamp.turn_on()
                self._state = 'on'
                self._pushed = False
            elif self._pushed and self._state == 'off':
                self._its_lamp.turn_off()
                self._state = 'off'
                self._pushed = False
            else:
                print("Button is not pushed", flush=True)
            sleep(30)