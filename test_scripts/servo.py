from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO


servo1 = Servo(12)
servo2 = Servo(13)
led = 2
val = -1
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)
increment = .1
"""
try:
    while True:
        servo1.value = val
        servo2.value = -val
        sleep(0.1)
        val = val + increment
        if val > .5:
            increment = -increment
            print(val)
        if val < 0:
            increment = -increment
            val = 0
            print(val)
except KeyboardInterrupt:
    print("Program stopped")
"""
servo1.value = val
sleep(.1) 
servo1.value = val + increment

servo2.value = 0
