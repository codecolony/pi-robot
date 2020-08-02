import RPi.GPIO as GPIO
import time as time
#from evdev import InputDevice, categorize, ecodes

GSPEED = 'high'  #current speed
ROT_DURA = 0.0	#current rotation duration

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11,GPIO.OUT)
	GPIO.setup(13,GPIO.OUT)
	GPIO.setup(15,GPIO.OUT)
	GPIO.setup(16,GPIO.OUT)
	GPIO.setup(32,GPIO.OUT)
	GPIO.setup(33,GPIO.OUT)
	f1 = GPIO.PWM(32,100)
	f2 = GPIO.PWM(33,100)
	f1.start(0)
	f2.start(0)
	reset()
	return f1,f2

def calibrate():
	global GSPEED
	global ROT_DURA

	if GSPEED=='vhigh':
		ROT_DURA = 0.35	
	elif GSPEED=='vlow':
		ROT_DURA = 2.4	
	elif GSPEED=='low':
		ROT_DURA = 2.0	
	elif GSPEED=='med':
		ROT_DURA = 0.6	
	elif GSPEED=='high':
		ROT_DURA = 0.7	
		
def speed(s,f1,f2):
	global GSPEED
	GSPEED = s

	if(s=='vlow'):
		f1.ChangeDutyCycle(10)
		f2.ChangeDutyCycle(10)
	elif(s=='low'):
		f1.ChangeDutyCycle(25)
		f2.ChangeDutyCycle(25)
	elif(s=='high'):
		f1.ChangeDutyCycle(75)
		f2.ChangeDutyCycle(75)
	elif(s=='vhigh'):
		f1.ChangeDutyCycle(100)
		f2.ChangeDutyCycle(100)
	elif(s=='med'):
		f1.ChangeDutyCycle(50)
		f2.ChangeDutyCycle(50)

	calibrate() 

def reset():
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)

def reverse(t):
	reset()
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	time.sleep(t)
	reset()

def forward(t):
	reset()
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	time.sleep(t)
	reset()

def left(t):
	reset()
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	time.sleep(t)
	reset()

def right(t):
	reset()
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	time.sleep(t)
	reset()

def clean_exit():
	GPIO.cleanup()
	f1.stop()
	f2.stop()

f1,f2 = init()

#gamepad = InputDevice('/dev/input/event0')

speed('med',f1,f2)
forward(1)
time.sleep(0.5)
left(3)
time.sleep(0.5)
right(3)
#reverse(1)
#for event in gamepad.read_loop():
#	print(event.code)
#	print(event.type)
#	if(event.type == ecodes.EV_KEY):
#		print(event)
#		if(event.value == 1):
#			if(event.code == 307):
#				forward(1)
#			if(event.code == 306):
#				print('right')
#				#right(1)
#			if(event.code == 305):
#				reverse(1)
#			if(event.code == 304):
#				print('left')
#				#left(1)
#			if(event.code == 309):
#				break
clean_exit()
