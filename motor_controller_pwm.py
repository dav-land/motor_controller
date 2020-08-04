#!/usr/bin/env python

import R64.GPIO as GPIO
from time import sleep
import rospy
from std_msgs.msg import Int32

class motor_control:
    def __init__(self):
        self.command_topic = '/motor_speed'
        self.sub = rospy.Subscriber(self.command_topic, Int32, self.speed_callback)

        print("Setting up GPIO pins")

        self.pwm_pin=16
        self.power_pin=18
        
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pwm_pin, GPIO.OUT)
        GPIO.setup(self.power_pin, GPIO.OUT, initial=GPIO.HIGH)

        print("Starting PWM output")
        self.p=GPIO.PWM(self.pwm_pin,50)
        self.p.start(50)


    def speed_callback(self, data):
        pwm_duty_cycle=data
        self.p.ChangeDutyCycle(pwm_duty_cycle)


    def shutdown_process(self):
        self.p.stop()
        GPIO.cleanup([self.pwm_pin,self.power_pin])
        print("Cleaning up pins")
        

if __name__ == "__main__":
    rospy.init_node('motor_node')
    obj = motor_control()
    rospy.spin()
    rospy.on_shutdown(self.shutdown_process)
        


    
