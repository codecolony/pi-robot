import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)



GPIO.output(11,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(16,GPIO.LOW)

GPIO.output(11,GPIO.HIGH)
GPIO.output(13,GPIO.LOW)
GPIO.output(15,GPIO.HIGH)
GPIO.output(16,GPIO.LOW)

time.sleep(3)

GPIO.output(11,GPIO.LOW)
GPIO.output(13,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(16,GPIO.LOW)

GPIO.output(11,GPIO.LOW)
GPIO.output(13,GPIO.HIGH)
GPIO.output(15,GPIO.LOW)
GPIO.output(16,GPIO.HIGH)

time.sleep(3)
GPIO.cleanup()
