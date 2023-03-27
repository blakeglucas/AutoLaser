from machine import Pin

class Laser(object):

    _lsr_pin: Pin

    def __init__(self, pin=2):
        self._lsr_pin = Pin(pin, mode=Pin.OUT, pull=Pin.PULL_UP)

    def on(self):
        self._lsr_pin.off()
    
    def off(self):
        self._lsr_pin.on()