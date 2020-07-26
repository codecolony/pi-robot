import RPi.GPIO as GPIO
import time as time

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)

def reset():
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)

def forward(t):
	reset()
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	time.sleep(t)

def reverse(t):
	reset()
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	time.sleep(t)

def left(t):
	reset()
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	time.sleep(t)

def right(t):
	reset()
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	time.sleep(t)

def clean_exit():
	GPIO.cleanup()

init()
forward(1)
reverse(1)
left(1)
right(1)
clean_exit()
