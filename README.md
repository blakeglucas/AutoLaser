# Auto Laser

An automatic laser pointer mover for your cat!

## Folders

### 3D

This folder contains the STL files for 3D printing and the FreeCAD source files for easy modification. Not every FreeCAD file has an associated STL because some are used as building blocks rather than as separate parts.

### Firmware

This folder contains the MicroPython firmware. This project was initially designed for the Pi Pico W, and the BaseMount part includes a corresponding mount, but you could modify it for use with another MicroPython compatible board (or just write your own firmware).

### PCB

This folder contains the design files for a Pi Pico (W) hat that makes connecting the laser and motors to the Pi Pico much easier. This part is not required.

## BOM

| Quantity      | Part        |
| --------------| ----------- |
| 2             | TowerPro SG-5010 (or body-compatible) servo motors    |
| 1     | Pi Pico W |
| 4     | M3x8 bolts    |
| 4     | M3 nuts   |
| 5     | M2x8 bolts    |
| 5     | M2 nuts   |
| 1     | Laser diode module        |
| 2     | Longer wires for the laser module |
| 1     | Micro-USB cable and wall plug |
| Any     | Cat |

> Servos: https://www.adafruit.com/product/155

> Laser Diodes: https://www.amazon.com/gp/product/B088PQQ9XV/

## Instructions

> If using a Pi Pico (W), be sure to flash MicroPython before starting. https://micropython.org/download/rp2-pico/

1. 3D print the STL files in the `3D` folder. Print plenty of extras of `ServoShaft` and `LaserArm`.
1. Connect your Pi Pico (W) to your computer and copy the Python files in the `Firmware` folder to your board, either via [Thonny](https://thonny.org/), [mpremote](https://docs.micropython.org/en/latest/reference/mpremote.html), or another way if you know one. After copying the files, disconnect your board from the computer.
1. (If using the PicoHat PCB) Solder the PicoHat to your Pi Pico (W).
1. Disassemble your servos and replace each drive shaft with the printed `ServoShaft` piece. It should be a drop-in replacement. Reassemble.
1. Attach the Pi Pico (W) to the `BaseMount` part using four of the M2 bolts and nuts. If you're using the PicoHat PCB, it's tricky to get the two by the micro-USB port, but it is doable.
1. Attach one of the servos to the `BaseMount` part using the M3 bolts and nuts.
1. (If necessary) De-solder the stock wires from the module and solder on two longer wires.
1. Snap the laser diode module into the `LaserHolder` part.
1. Attach the `LaserHolder` part to the `LaserArm` part using the remaining M2 bolt and nut.
1. Slide the `LaserArm` part onto the free servo's shaft at as close to a 90 degree angle as you can get.
1. Insert the free servo with the `LaserArm` attached into the `YMount` part.
1. Attach the now-assembled `YMount` part to `BaseMount`.
1. Slide the servo and laser wires through the slit on the back of `BaseMount` and attach them to your Pi Pico (W), either via the provided PicoHat or another method.
1. Connect your board to a power source. The servos will be driven to the zero position (50% duty), pause for five seconds, then begin the random laser movement.

## 3D Printing Instructions

> If you haven't tried the "Lightning" fill pattern in PrusaSlicer/SuperSlicer, give it a shot.

### BaseMount

Print top-face-down, using supports for only the counterbore screw holes on the face. Any infill, any layer height (0.2mm recommended).

### LaserArm

Print with the gear attachment hole facing up. Use support for only the counterbore screw hole. Sparse infill is fine, any layer height (18% and 0.2mm recommended, respectively).

### LaserHolder

Print the obvious orientation. No supports required. A finer layer height could be beneficial, but 0.2mm will work just fine.

### ServoShaft

If you have a printer with a 0.2-0.25mm nozzle, that is preferable, but a 0.4mm nozzle will work too. Add a support enforcer for the large negative area inside the gear, but support is not required for inside the smaller hole. 0.2mm layer height recommended, 100% infill for strength.

### YMount

Print the obvious orientation. Use support for the inset hole but not for inside the gear hole. Sparse infill, 0.2mm layer height recommended.
