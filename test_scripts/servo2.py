from gpiozero import Servo
from time import sleep
import RPi.GPIO as GPIO
import numpy as np

positions = [*np.linspace(0,1,10), *np.linspace(0,1,100)]
servo1 = Servo(12)
servo2 = Servo(13)
led = 2
val = -1
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)
increment = .1
servo1.min()
servo2.min()
sleep(2)
servo1.max()
servo2.max()
sleep(2)

for pos in positions:
    print(pos)
    servo2.value = pos
    servo1.value = pos
    sleep(0.5)
