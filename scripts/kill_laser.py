import RPi.GPIO as GPIO
led = 2
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 0)
print("Turned off Laser")

