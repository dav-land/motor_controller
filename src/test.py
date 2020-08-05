import R64.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)

p = GPIO.PWM(16, 50)
p.start(0)
sleep(5)
p.ChangeDutyCycle(20)
sleep(5)
p.ChangeDutyCycle(40)
sleep(5)
p.ChangeDutyCycle(60)
sleep(5)
p.ChangeDutyCycle(80)
sleep(5)
p.ChangeDutyCycle(98)
sleep(5)
p.stop()
GPIO.cleanup()
