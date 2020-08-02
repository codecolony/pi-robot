import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
p = GPIO.PWM(8, 50)

p.start(7.5)

p.ChangeDutyCycle(7.5)
time.sleep(1)
p.ChangeDutyCycle(12.5)
time.sleep(1)
p.ChangeDutyCycle(2.5)
time.sleep(1)
p.ChangeDutyCycle(7.5)
time.sleep(1)

p.stop()
GPIO.cleanup()
