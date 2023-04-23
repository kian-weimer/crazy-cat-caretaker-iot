import argparse
from time import sleep
from gpiozero import Motor

def run_motor(time_to_run):
    motor = Motor("GPIO20","GPIO26")
    motor.forward(speed=1)
    sleep(time_to_run)
    motor.stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", help="time to run the motor (in seconds)", type=int, default=2)
    args = parser.parse_args()
    run_motor(args.time)

