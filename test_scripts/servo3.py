#!/usr/bin/python3
import RPi.GPIO as GPIO
import pigpio
import time

servo = 12

# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm2 = pigpio.pi()
pwm2.set_mode(servo+1, pigpio.OUTPUT)

pwm2.set_PWM_frequency( servo+1, 50 )
pwm.set_PWM_frequency( servo, 50 )

# print( "0 deg" )
# pwm.set_servo_pulsewidth( servo, 500 ) ;
# time.sleep( 3 )

print( "90 deg" )
pwm.set_servo_pulsewidth( servo, 1500 ) ;

pwm.set_PWM_frequency( servo+1, 50 )

print( "90 deg" )
pwm.set_servo_pulsewidth( servo+1, 2500 ) ;
time.sleep( 3 )

pwm.set_PWM_frequency( servo, 50 )
print( "180 deg" )

pwm.set_servo_pulsewidth( servo+1, 1500 ) ;

pwm.set_PWM_frequency( servo+1, 50 )
print( "180 deg" )

pwm.set_servo_pulsewidth( servo, 2500 ) ;
time.sleep( 3 )

# turning off servo
pwm.set_PWM_dutycycle( servo, 0 )
pwm.set_PWM_frequency( servo, 0 )


# turning off servo
pwm2.set_PWM_dutycycle( servo, 0 )
pwm2.set_PWM_frequency( servo, 0 )
