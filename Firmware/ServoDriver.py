from machine import Pin, PWM
import time
import uasyncio

SERVO_MIN_DUTY = 0.2
SERVO_MAX_DUTY = 0.95
SERVO_FREQ = 400
SERVO_DUTY_DELTA = SERVO_MAX_DUTY - SERVO_MIN_DUTY
SERVO_ZERO_DUTY = SERVO_DUTY_DELTA / 2.0
INT_U16_MAX = (1 << 16) - 1


class ServoDriver(object):

    pct_max: float = 100
    pct_min: float = 0
    ctrl_pwm: PWM

    _cur_pct: float

    def __init__(self, pin: int, pct_range: tuple[float, float] | None = None):
        if pct_range:
            self.pct_max = max(pct_range)
            self.pct_min = min(pct_range)
        self.ctrl_pwm = PWM(Pin(pin, mode=Pin.OUT))
        self.ctrl_pwm.freq(SERVO_FREQ)
        self.duty_pct(50)

    def duty_pct(self, pct: float):
        if pct > self.pct_max:
            pct = self.pct_max
        elif pct < self.pct_min:
            pct = self.pct_min
        self._cur_pct = pct
        factor = (SERVO_DUTY_DELTA * pct / 100.0) + SERVO_MIN_DUTY
        self.ctrl_pwm.duty_u16(int(INT_U16_MAX * factor))

    async def move(self, target_pct: float, time_s: float, timestep=0.01):
        # Enforce here as well to keep timing consistent
        if target_pct < self.pct_min:
            target_pct = self.pct_min
        elif target_pct > self.pct_max:
            target_pct = self.pct_max
        delta_target = target_pct - self._cur_pct
        step_pct = delta_target * timestep / time_s
        time_ctr = 0
        while time_ctr <= time_s:
            self.duty_pct(self._cur_pct + step_pct)
            await uasyncio.sleep(timestep)
            time_ctr += timestep
