from time import sleep
from gpiozero import Motor

motor = Motor("GPIO20","GPIO26")

motor.forward(speed =.5)
motorSpeedForward = .5
motorSpeedBackward = 0
def forwardSpeedIncrease():
    global motorSpeedForward
    motor.forward(speed=motorSpeedForward)
    print("Increased speed of motor backward. Current speed = "+ str(motorSpeedForward))
    motorSpeedForward += 0.1
    if motorSpeedForward >= 1:
        motorSpeedForward = 1

def forwardSpeedReduce():
    global motorSpeedForward
    motor.forward(speed=motorSpeedForward)
    print("Reduce speed of motor forward. Current speed = "+ str(motorSpeedForward))
    motorSpeedForward -= 0.1
    if motorSpeedForward <= 0:
        motorSpeedForward = 0

def backwardSpeedIncrease():
    global motorSpeedBackward
    motor.forward(speed=motorSpeedBackward)
    print("Increased speed of motor backward. Current speed = "+ str(motorSpeedBackward))
    motorSpeedBackward += 0.1
    if motorSpeedBackward >= 1:
        motorSpeedBackward = 1

def backwardSpeedReduce():
    global motorSpeedBackward
    motor.backward(speed=motorSpeedBackward)
    print("Reduce speed of motor backward. Current speed = "+ str(motorSpeedBackward))
    motorSpeedBackward -= 0.1
    if motorSpeedBackward <= 0:
        motorSpeedBackward = 0

print("start")
'''
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
forwardSpeedIncrease()
'''
backwardSpeedIncrease()
backwardSpeedIncrease()
backwardSpeedIncrease()
backwardSpeedIncrease()
backwardSpeedIncrease()

backwardSpeedIncrease()
backwardSpeedIncrease()
backwardSpeedIncrease()
backwardSpeedIncrease()
backwardSpeedIncrease()
backwardSpeedIncrease()

backwardSpeedIncrease()



while(True):
    sleep(.1)
