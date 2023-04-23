import RPi.GPIO as gp  
from time import sleep
pin = 12
gp.setmode(gp.BCM)  
gp.setup(pin,gp.OUT)  
pwm=gp.PWM(pin,50)  
pwm.start(0)  
for i in range(0,181):  
    print("here")
    sig=(i/18)+2  
    pwm.ChangeDutyCycle(sig)  
    sleep(0.03)  
for i in range(180,-1,-1):  
    sig=(i/18)+2  
    pwm.ChangeDutyCycle(sig)  
    sleep(0.03)  
pwm.stop()  
gp.cleanup()
print("Finished")
