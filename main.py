import RPi.GPIO as GPIO
import time as time

#from evdev import InputDevice, categorize, ecodes

def init():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3,GPIO.OUT) # left trigger
	GPIO.setup(5,GPIO.IN) # left echo
 
	GPIO.setup(7,GPIO.OUT) # mid trigger
	GPIO.setup(10,GPIO.IN) # mid echo

	GPIO.setup(8,GPIO.OUT) # right trigger
	GPIO.setup(12,GPIO.IN) # right echo

	GPIO.setup(11,GPIO.OUT)# Left motor pin
	GPIO.setup(13,GPIO.OUT) # "
	GPIO.setup(15,GPIO.OUT) # Right Motor PIn
	GPIO.setup(16,GPIO.OUT) # "
	GPIO.setup(32,GPIO.OUT) # Left Motor Pwm
	GPIO.setup(33,GPIO.OUT) # Right Motor Pwm

	f1 = GPIO.PWM(32,100)
	f2 = GPIO.PWM(33,100)
	f1.start(0)
	f2.start(0)
	reset()
	return f1,f2

def getDistance(t,e):
	time.sleep(0.1)
	GPIO.output(t,1)
	time.sleep(0.00001)
	GPIO.output(t,0)
	while GPIO.input(e) == False:
		pass
	start = time.time()
	while GPIO.input(e) == True:
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

def reset():
	GPIO.output(11,GPIO.LOW)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.LOW)

def forward(t):
	reset()
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(13,GPIO.LOW)
	GPIO.output(15,GPIO.LOW)
	GPIO.output(16,GPIO.HIGH)
	
def reverse(t):
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
	time.sleep(t)
	reset()

def right_turn(t):
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
speed('med',f1,f2)
time.sleep(0.5)
forward(1)

while True:
	leftdist = getDistance(3,5)
	#print('Left='+str(leftdist))
	middist = getDistance(7,10)
	#print('Mid='+str(middist))
	rightdist = getDistance(8,12)
	print('Left='+str(leftdist)+' Mid='+str(middist)+' Right='+str(rightdist))

	if leftdist<=20 or rightdist<=20 or middist<=40:
		if leftdist>rightdist:
			left_turn(1)
		elif rightdist>leftdist:
			right_turn(1)
		elif middist<=40:
			reverse(2)
			continue
			 
clean_exit()

###########################################################
#reverse(1) for event in gamepad.read_loop():
#	print(event.code) print(event.type) if(event.type == ecodes.EV_KEY):
#		print(event) if(event.value == 1):
#			if(event.code == 307):
#				forward(1) if(event.code == 306): print('right')
#				#right(1)
#			if(event.code == 305):
#				reverse(1) if(event.code == 304): print('left')
#				#left(1)
#			if(event.code == 309):
#				break
