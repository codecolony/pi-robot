import RPi.GPIO as GPIO
import time as time

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(32,GPIO.OUT)
	GPIO.setup(33,GPIO.OUT)
	f1  = GPIO.PWM(32,100)
	f2  = GPIO.PWM(33,100)
	f1.start(0)
	f2.start(0)
	return f1,f2

def speed(s,f1,f2):
	if(s=='vlow'):
		f1.ChangeDutyCycle(10)
		f2.ChangeDutyCycle(10)
	if(s=='low'):
		f1.ChangeDutyCycle(25)
		f2.ChangeDutyCycle(25)
	if(s=='high'):
		f1.ChangeDutyCycle(75)
		f2.ChangeDutyCycle(75)
	if(s=='vhigh'):
		f1.ChangeDutyCycle(100)
		f2.ChangeDutyCycle(100)
	if(s=='med'):
		f1.ChangeDutyCycle(50)
		f2.ChangeDutyCycle(50)

def reset():
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)

def reverse(t):
	reset()
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	time.sleep(t)
	reset()

def forward(t):
	reset()
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	time.sleep(t)
	reset()

def left(t):
	reset()
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	time.sleep(t)
	reset()

def right(t):
	reset()
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	time.sleep(t)
	reset()

def clean_exit():
	GPIO.cleanup()
	f1.stop()
	f2.stop()

f1,f2 = init()
speed('vlow',f1,f2)
forward(2)

speed('low',f1,f2)
forward(2)


speed('med',f1,f2)
forward(2)

speed('high',f1,f2)
forward(2)

speed('vhigh',f1,f2)
forward(2)

#reverse(1)
#left(1)
#right(1)
clean_exit()
