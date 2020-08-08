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
	GPIO.setup(8,GPIO.OUT) # Servo Motor Pin
	GPIO.setup(11,GPIO.OUT) # Left Motor Pin
	GPIO.setup(13,GPIO.OUT) # "
	GPIO.setup(15,GPIO.OUT) # Right Motor PIn
	GPIO.setup(16,GPIO.OUT) # "
	GPIO.setup(32,GPIO.OUT) # Left Motor Pwm
	GPIO.setup(33,GPIO.OUT) # Right Motor Pwm
	f1 = GPIO.PWM(32,100)
	f2 = GPIO.PWM(33,100)
	m = GPIO.PWM(8,50)
	f1.start(0)
	f2.start(0)
	m.start(0)
	reset()
	return f1,f2,m

def getDistance():
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

f1,f2,m = init()
speed('high',f1,f2)
#print('distance='+str(getDistance()))
m.ChangeDutyCycle(6.5)
time.sleep(0.5)
reverse(1)
while True:
	dist = getDistance()
	if(dist < STOP_DIST):
		reset()
		m.ChangeDutyCycle(3.5)
		right = getDistance()
		time.sleep(0.3)
		m.ChangeDutyCycle(9.5)
		left = getDistance()
		time.sleep(0.3)
		m.ChangeDutyCycle(6.5)
		time.sleep(0.3)
		if left > right:
			#speed('high',f1,f2)
			left_turn(0.5)
			#speed('low',f1,f2)
			reverse(1)
		elif right > left:
			#speed('high',f1,f2)
			right_turn(0.5)
			#speed('low',f1,f2)
			reverse(1)
		elif left < STOP_DIST and right < STOP_DIST:
			break;
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
