from Laser import Laser
from random import randrange
from ServoDriver import ServoDriver
import time
import uasyncio

# Y Driver max range: 10-90
# Y Driver effective range: 50-75 !! this depends on LaserHolder attachment angle and your play space
X_RANGE = (0, 100)
Y_RANGE = (60, 90)

async def main():
    lsr = Laser()
    lsr.off()
    x_drv = ServoDriver(0, X_RANGE)
    y_drv = ServoDriver(1, Y_RANGE)
    time.sleep(5)
    lsr.on()
    while True:
        x_pos = randrange(*X_RANGE)
        y_pos = randrange(*Y_RANGE)
        x_time = randrange(1, 5)
        delay = randrange(100, 1000)
        x_task = uasyncio.create_task(x_drv.move(x_pos, x_time))
        y_task = uasyncio.create_task(y_drv.move(y_pos, x_time))
        await uasyncio.gather(x_task, y_task)
        print(x_pos, y_pos, x_time, delay)
        time.sleep(delay / 1000.0)

uasyncio.run(main())
