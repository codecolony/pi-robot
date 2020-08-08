import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

GPIO.setup(3,GPIO.IN)

GPIO.setup(5,GPIO.OUT)
GPIO.output(5,0)

time.sleep(0.1)

GPIO.setup(8, GPIO.OUT)

def getDistance():
	GPIO.output(5,1)
	time.sleep(0.00001)
	GPIO.output(5,0)
	print('reading input')
	while GPIO.input(3) == False:
		pass
	start = time.time()
	print('in second while loop')
	while GPIO.input(3) == True:
		pass
	end = time.time()
	print('start='+str(start))
	print('end='+str(end))
	return (end-start)*17000

p = GPIO.PWM(8, 50)

p.start(0)

i=2
while i<=12:
	p.ChangeDutyCycle(i)
	print('DC='+str(i))
	print(getDistance())
	time.sleep(1)
	i=i+1

p.stop()
GPIO.cleanup()
