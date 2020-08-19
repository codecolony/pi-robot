import RPi.GPIO as GPIO
import time as time
#from evdev import InputDevice, categorize, ecodes

GSPEED = 'high'  #current speed
ROT_DURA = 0.0	#current rotation duration
STOP_DIST = 55
def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3,GPIO.IN) # ECHO PIN, Distance sensor
	GPIO.setup(5,GPIO.OUT) # Trigger pin 
	
def getDistance_mid():
	time.sleep(0.1)
	GPIO.output(5,1)
	time.sleep(0.00001)
	GPIO.output(5,0)
	while GPIO.input(3) == False:
		pass
	start = time.time()
	while GPIO.input(3) == True:
		pass
	end = time.time()
	return (end-start)*17150

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
		ROT_DURA = 0.6	
		
def speed(s,f1,f2):
	global GSPEED
	GSPEED = s
	if(s=='vlow'):
		f1.ChangeDutyCycle(10)
		f2.ChangeDutyCycle(10)
	elif(s=='low'):
		f1.ChangeDutyCycle(20)
		f2.ChangeDutyCycle(20)
	elif(s=='high'):
		f1.ChangeDutyCycle(65)
		f2.ChangeDutyCycle(65)
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
	
def forward(t):
	reset()
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)

def left_turn(t):
	reset()
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.HIGH)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	time.sleep(ROT_DURA)
	reset()

def right_turn(t):
	reset()
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(16,GPIO.LOW)
	time.sleep(ROT_DURA)
	reset()

def clean_exit():
	GPIO.cleanup()
	f1.stop()
	f2.stop()

def smooth_turn(f1,f2):
	reset()
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	f1.ChangeDutyCycle(1)
	f2.ChangeDutyCycle(35)
	

init()

clean_exit()

###########################################################
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
