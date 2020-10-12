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

 
#setting lengths for arms
a1 = 5.07
a2= 3.81
wait_time = .2

#setting unit step of letters
unitstep = 1

#######################
## FIND MOTOR ANGLES ##
#######################
def getAngles(x,y):

   ''' 
    a = math.sqrt(-(a1**2) * (y**2) * ((a1**4) + (-(a2**2) + (x**2) + (y**2))**2 - 2*(a1**2)*((a2**2) + (x**2) + (y**2))))
    b1 = 1 / ((a1**2)*((x**2) + (y**2)))
    b2 = 1 / ((a1**2)*((x**2) + (y**2)) * y)
    c1 = (a1**3)*x + a1*x*(-(a2**2) + (x**2) + (y**2))
    c2 = (a1**3)*(y**2) + a1*(y**2)*(-(a2**2) + (x**2) + (y**2))

    g1 = b1*(c1+a)
    g2 = b2*(c2-x*a)
    theta1 =math.atan2(g1, g2) * 180/3.141592

    h = (-(a1**2)-(a2**2)+(x**2)+(y**2))/(a1*a2)
    j = a/((a1**2)*a2*y)

    theta2 = math.atan2(h,j) * 180/3.141592
'''

    t1 = math.pi/2 - math.atan2( (a1**3*x + a1*x*(-a2**2 + x**2 + y**2) + \
     math.sqrt(-(a1**2*y**2*(a1**4 + (-a2**2 + x**2 + y**2)**2 - \
     2*a1**2*(a2**2 + x**2 + y**2)))))/(a1**2*(x**2 + y**2)),\
     (a1**3*y**2 + a1*y**2*(-a2**2 + x**2 + y**2) - \
     x*math.sqrt(-(a1**2*y**2*(a1**4 + (-a2**2 + x**2 + y**2)**2 -\
     2*a1**2*(a2**2 + x**2 + y**2)))))/(a1**2*y*(x**2 + y**2)))

    t2 = math.acos((x**2 + y**2 - a1**2 - a2**2)/(2 * a1 * a2))

   # print(theta1, theta2)

    t11 = t1 * 180/3.141592
    t22 = t2 * 180/3.141592
    return t11, t22


'''

VERSION 2: Not Suitable
    if x < 0:
        xnew = abs(x)
    else:
        xnew = x
    a = (x**2) + (y**2) - (length1**2) - (length2**2)
    #print(a)
    b = (2*length2*length1)
    #print(b)
    c = a/b
    #print(c)
    print("A B C are " + str(a) + " "+ str(b) + " " + str(c))
    theta2 = math.acos(c)
    
    print("THETA 2 is " + str(theta2))
    g = length1 + length2*math.cos(theta2)
    h = g*(y-g)/(length2*math.sin(theta2))
    j = h - length2*math.sin(theta2)
    print(j)
    print(xnew/j)
    if x < 0:
        theta1 = 180 - (math.asin(xnew / j) * 180/3.141592)
    else:
        theta1 = math.asin(xnew / j) * 180/3.141592

    theta2 = theta2 * 180/3.141592
    print(str(theta1) + "," + str(theta2))
    return theta1 , theta2
'''

####################
## MAIN FUNCTIONS ##
####################

'''
Test Function 1 with offsets
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
'''
elbow.angle = 0
input ("0")

elbow.angle = (18/13)*90

input("90")

elbow.angle = (18/13)*130 

input("180")

elbow.angle = (18/13)*90
'''

'''
Test Function 2 with Offsets
t1 = 0
t2 = 0
shoulder.angle = t1*(-2/3) + 120
elbow.angle = (18/13)*t2

input("30?")

t1 = 30
t2 = 30
shoulder.angle = t1*(-2/3) + 120
elbow.angle = (18/13)*t2

input("60")

t1 = 60
t2 = 60
shoulder.angle = t1*(-2/3) + 120
elbow.angle = (18/13)*t2

input("90")

t1 = 90
t2 = 90
shoulder.angle = t1*(-2/3) + 120
elbow.angle = (18/13)*t2

input("120")

t1 = 120
t2 = 120
shoulder.angle = t1*(-2/3) + 120
elbow.angle = (18/13)*t2
'''

#easily continuously run-able test function
shoulder.angle = 0
elbow.angle = 0

while True:
   x = float((input("X Coord? ")))
   y = float((input("Y Coord? ")))
   theta1 , theta2 = getAngles(x,y)
   print("T1: " + str(theta1) + " , T2: " + str(theta2))
   shoulder.angle = theta1
   elbow.angle = theta2



