import RPi.GPIO as GPIO
import pigpio
import time
import argparse

# Define the argument parser
parser = argparse.ArgumentParser(description='Laser Code')

# Add arguments
parser.add_argument('-m', '--mode', type=str, required=False, default="RANDOM",
                    help='mode to run program with')

# Parse the arguments
args = parser.parse_args()

# Access the values of the arguments

mode = args.mode



led = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, 1)
ZERO_FREQUENCY = 500
HALF_FREQUENCY = 1500
FULL_FREQUENCY = 2500
SERVO12 = 12
SERVO13 = 13
path_dict = {}
# Randomish and longer path
path_dict["random"] = [(0, 0.25, 0.25), (0, 0.5, 2), (0.5,0.8,3), (0.5, 0.25, 0.5), (0.1, 0.5, 0.8),
	(0.2, 0.85, 0.02), (0.6, 0.5, 2), 
	 (0, 0.75, 1), (0, 0.5, 0.25), (0.25, 0.5, 0.25), (0.25,0.25,0.25)]

# Side to side 
path_dict["side_side"] = [(0.25, 0.15, 0.5), (0.25, 0.85, 0.5)]

# Circle
path_dict["circle"] = [(0.4, 0.2, 0.05), (0.3, 0.2, 0.05), (0.2, 0.2, 0.05), (0.1, 0.25, 0.05), (0.05, 0.3, 0.05),
	 (0, 0.35, 0.05), (0, 0.4, 0.05), (0, 0.45, 0.05), (0, 0.5, 0.05), (0, 0.55, 0.05),
	 (0, 0.6, 0.05), (0, 0.65, 0.05), (0.05, 0.7, 0.05), (0.1, 0.75, 0.05), (0.2, 0.8, 0.05), 
	(0.3, 0.8, 0.05), (0.4, 0.8, 0.05), (0.5, 0.75, 0.05), (0.6, 0.7, 0.05), (0.7, 0.65, 0.05),
	(0.75, 0.6, 0.05), (0.75, 0.55, 0.05), (0.75, 0.5, 0.05), (0.75, 0.45, 0.05), (0.75, 0.4, 0.05),
	(0.75, 0.35, 0.05), (0.7, 0.3, 0.05), (0.6, 0.25, 0.05), (0.5, 0.25, 0.05)]

# Up and down

path_dict["up_down"] = [(0,0.5,1), (0.8,0.5,1)]

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


def run_laser(mode:str):
    pwm = init_pwm()
    for pos in path_dict[mode]:
        print(pos)
        move_servos(pwm, pos)
    done(pwm)


if __name__ == "__main__":
	try:
		while True:
			run_laser(mode)
	except:
		GPIO.output(led, 0)


