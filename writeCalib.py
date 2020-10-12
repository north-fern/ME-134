## LETTERS ##
import math
import time
from adafruit_motor import servo
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import RPi.GPIO as GPIO

#setting up serial communication with servo board
i2c_bus  = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50

# declaring servos
shoulder = servo.Servo(pca.channels[0])
elbow= servo.Servo(pca.channels[4])
#pen = servo.Servo(pca.channels[6])
 
#setting lengths for arms
length1 = 8
length2 = 15
wait_time = .2

#setting unit step of letters
unitstep = 6

#setting up button
#https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#set to pin 10 - connect from pin 10 to 3.3 power w/ resistor

#######################
## FIND MOTOR ANGLES ##
#######################
def getAngles(x,y):
    a = (x^2) + (y^2) - (length1^2) - (length2^2)
    #print(a)
    b = (2*length2*length1)
    #print(b)
    c = a/b
    #print(c)
    print("A B C are " + str(a) + " "+ str(b) + " " + str(c))
    theta2 = math.acos(c)
    print("THETA 2 is " + str(theta2))
    d = length1 + length2*math.cos(theta2)
    #print(d)
    e = length2*math.sin(theta2)*((x + length2*math.sin(theta2))/(length1 + length2*math.cos(theta2)))
    #print(e)
    if e == 0:
        h = 0
    else:
        h = y/(d*e)
    print("D and E are " + str(d) + " " + str(e))
    theta1 = math.asin(h) * 180/3.141592
    theta2 = theta2 * 180/3.141592
    print(str(theta1) + "," + str(theta2))
    return theta1 , theta2

####################
## MAIN FUNCTIONS ##
####################

'''
x1 = 0
y1 = 0
t1 = 0
shoulder.angle = t1*(-2/3) + 120
elbow.angle = 0

input("WAIT")

shoulder.angle = 1*(-2/3) + 120

input("WAIT")
t1 = 90
shoulder.angle = t1*(-2/3) + 120
elbow.angle = 0

input("WAIT")
t1,t2 = getAngles(5,5)
shoulder.angle = t1*(-2/3) + 120
time.sleep(.5)
elbow.angle = t2
time.sleep(.5)

t1,t2 = getAngles(5,6)
shoulder.angle = t1*(-2/3) + 120
time.sleep(.5)
elbow.angle = t2
time.sleep(.5)

t1,t2 = getAngles(6,6)
shoulder.angle= t1*(-2/3) + 120
time.sleep(.5)
elbow.angle = t2
time.sleep(.5)

t1,t2 = getAngles(6,5)
shoulder.angle = t1*(-2/3) + 120
time.sleep(.5)
elbow.angle = t2
time.sleep(.5)

t1,t2 = getAngles(5,5)
shoulder.angle = t1*(-2/3) + 120
time.sleep(.5)
elbow.angle = t2
time.sleep(.5)
'''

elbow.angle = 0
input ("0")

elbow.angle = 90

input("90")

elbow.angle = 180 

input("180")

elbow.angle = 90