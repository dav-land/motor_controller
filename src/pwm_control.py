#!/usr/bin/env python                                                                                   

import R64.GPIO as GPIO
from time import sleep
import rospy
from std_msgs.msg import Int32

pwm_pin=16
power_pin=18
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(power_pin, GPIO.OUT, initial=GPIO.HIGH)

print("Starting PWM output")
p=GPIO.PWM(pwm_pin,50)
p.start(0)


def speed_callback(msg):
    num = msg.data
    p.ChangeDutyCycle(num)
    print("Changing Duty Cycle")
    print(num)



if __name__ == "__main__":
    rospy.init_node("spinny")

    print("Setting up GPIO pins")
    
    sub = rospy.Subscriber('/motor_speed', Int32, speed_callback)

    rospy.spin()

    p.stop()
    GPIO.cleanup()
