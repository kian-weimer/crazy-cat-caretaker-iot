import RPi.GPIO as GPIO
import pigpio
import time

led = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)
ZERO_FREQUENCY = 500
HALF_FREQUENCY = 1500
FULL_FREQUENCY = 2500
SERVO12 = 12
SERVO13 = 13

path = [(0, 0, 3), (0.5, 0.5, 3), (0.75, 0.75, 3), (1, 1, 3)] 
	# 	(0, 0, 0.5), (0.5, 0.5, 0.5), (0.75, 0.75, 0.5), (1, 1, 0.5)]

def init_pwm():
	pwm = pigpio.pi()
	pwm.set_mode(SERVO12, pigpio.OUTPUT)
	pwm.set_PWM_frequency( SERVO12, 50 )
	return pwm

def done(pwm):
	pwm.set_PWM_dutycycle( SERVO12, 0 )
	pwm.set_PWM_frequency( SERVO12, 0 )
	pwm.set_PWM_dutycycle( SERVO13, 0 )
	pwm.set_PWM_frequency( SERVO13, 0 )

def servo12_frequency(percent):
	return percent * (FULL_FREQUENCY - HALF_FREQUENCY) + HALF_FREQUENCY

def servo13_frequency(percent):
	return percent * (FULL_FREQUENCY - ZERO_FREQUENCY) + ZERO_FREQUENCY

def move_servos(pwm, position):
	servo12_position, servo13_position, delay = position
	servo12_position = servo12_frequency(servo12_position)
	servo13_position = servo13_frequency(servo13_position)

	pwm.set_servo_pulsewidth( SERVO12, servo12_position ) ;
	pwm.set_servo_pulsewidth( SERVO13, servo13_position ) ;
	time.sleep(delay)


def test():
    pwm = init_pwm()
    for pos in path:
        print(pos)
        move_servos(pwm, pos)
    done(pwm)
    GPIO.output(led, 0)


if __name__ == "__main__":
	test()

