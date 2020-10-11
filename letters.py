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
elbow= servo.Servo(pca.channels[3])
pen = servo.Servo(pca.channels[6])
 
#setting lengths for arms
length1 = 1
length2 = 2

#setting unit step of letters
unitstep = 1

#setting up button
#https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
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
    theta2 = math.acos(c)
    print("THETA 2 is " + str(theta2))
    d = length1 + length2*math.cos(theta2)
    print(d)
    e = length2*math.sin(theta2)*((x + length2*math.sin(theta2))/(length1 + length2*math.cos(theta2)))
    print(e)
    if e == 0:
        h = 0
    else:
        h = y/(d*e)

    theta1 = math.asin(h)
    print(str(theta1) + "," + str(theta2))
    return theta1, theta2

#####################
## PEN DEFINITIONS ##
#####################
def pen_up():
    '''
    i = 0
    while GPIO.input(10) != GPIO.HIGH:
        pen.angle() = i+1
        i = i + 1
        '''
    
def pen_down():
    '''
        i = 50
    while GPIO.input(10) != GPIO.HIGH:
        pen.angle() = i-1
        i = i - 1
        '''

######################
## MOTION FUNCTIONS ##
######################
def up(x, y, WRITE_BOOL):
    nx = x
    ny = y + unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    time.sleep(.1)
    elbow.angle = an2
    time.sleep(.1)
    print(str(nx) + "," + str(ny))
    return nx,ny

def down(x, y, WRITE_BOOL):
     
    nx = x
    ny = y - unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    time.sleep(.1)
    elbow.angle = an2
    time.sleep(.1)
    print(str(nx) + "," + str(ny))
    return nx,ny

def left(x, y, WRITE_BOOL):
    
    nx = x - unitstep
    ny = y 
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    time.sleep(.1)
    elbow.angle = an2
    time.sleep(.1)
    print(str(nx) + "," + str(ny))
    return nx,ny

def right(x, y, WRITE_BOOL):
    
    nx = x + unitstep
    ny = y 
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    time.sleep(.1)
    elbow.angle = an2
    time.sleep(.1)
    print(str(nx) + "," + str(ny))
    return nx,ny

def down_diag_l2r(x, y, WRITE_BOOL):
    
    nx = x + unitstep
    ny = y - unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    time.sleep(.1)
    elbow.angle = an2
    time.sleep(.1)
    print(str(nx) + "," + str(ny))
    return nx,ny

def down_diag_r2l(x, y, WRITE_BOOL):
    
    nx = x - unitstep
    ny = y - unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    time.sleep(.1)
    elbow.angle = an2
    time.sleep(.1)
    print(str(nx) + "," + str(ny))
    return nx,ny

def up_diag_l2r(x, y, WRITE_BOOL):
    
    nx = x + unitstep
    ny = y + unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    time.sleep(.1)
    elbow.angle = an2
    time.sleep(.1)
    print(str(nx) + "," + str(ny))
    return nx,ny

def up_diag_r2l(x, y, WRITE_BOOL):
    
    nx = x - unitstep
    ny = y + unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    time.sleep(.1)
    elbow.angle = an2
    time.sleep(.1)
    print(str(nx) + "," + str(ny))
    return nx,ny

#######################
## LETTER DEFINITONS ##
#######################
def A(x, y):
    '''
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,T)
    x6,y6 = down(x5,y5,T)
    x7,y7 = up(x6,y6,F)
    x8,y8 = left(x7,y7,T)
    x9,y9 = left(x8,y8,T)
    x10,y10 = down_diag_l2r(x9,y9,F)
    x11,y11 = right(x10,y10,F)
    ex,ey = right(x11,y11,F)
    '''
    ex,ey = up(0,0,T)
    return ex,ey

def B(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,T)
    x6,y6 = down(x5,y5,T)
    x7,y7 = up(x6,y6,F)
    x8,y8 = left(x7,y7,T)
    x9,y9 = left(x8,y8,T)
    x10,y10 = down(x9,y9,F)
    x11,y11 = right(x10,y10,T)
    x12,y12 = right(x11,y11,T)
    ex,ey = right(x12,y12,F)
    return ex,ey

def C(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,F)
    x6,y6 = down(x5,y5,F)
    x7,y7 = left(x6,y6,T)
    x8,y8 = left(x7,y7,T)
    x9,y9 = right(x8,y8,F)
    x10,y10 = right(x9,y9,F)
    ex,ey = right(x10,y10,F)
    return ex,ey

def E(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,F)
    x6,y6 = left(x5,y5,T)
    x7,y7 = left(x6,y6,T)
    x8,y8 = down(x7,y7,F)
    x9,y9 = right(x8,y8,T)
    x10,y10 = right(x9,y9,T)
    ex,ey = right(x10,y10,F)
    return ex,ey

def F(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,F)
    x6,y6 = left(x5,y5,T)
    x7,y7 = left(x6,y6,T)
    x8,y8 = down(x7,y7,F)
    x9,y9 = right(x8,y8,F)
    x10,y10 = right(x9,y9,F)
    ex,ey = right(x10,y10,F)
    return ex,ey

def G(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,F)
    x6,y6 = down(x5,y5,T)
    x7,y7 = left(x6,y6,T)
    x8,y8 = left(x7,y7,F)
    x9,y9 = down(x8,y8,F)
    x10,y10 = right(x9,y9,T)
    x11,y11 = right(x10,y10,T)
    ex,ey = right(x11,y11,F)
    return ex,ey

def H(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,F)
    x4,y4 = right(x3,y3,F)
    x5,y5 = down(x4,y4,T)
    x6,y6 = down(x5,y5,T)
    x7,y7 = up(x6,y6,F)
    x8,y8 = left(x7,y7,T)
    x9,y9 = left(x8,y8,T)
    x10,y10 = down(x9,y9,F)
    x11,y11 = right(x10,y10,F)
    x12,y12 = right(x11,y11,F)
    ex,ey = right(x12,y12,F)
    return ex,ey

def I(x, y):
    x1,y1 = right(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,T)
    x6,y6 = down(x5,y5,T)
    x7,y7 = up(x6,y6,F)
    x8,y8 = left(x7,y7,T)
    x9,y9 = left(x8,y8,T)
    x10,y10 = down(x9,y9,F)
    x11,y11 = right(x10,y10,T)
    x12,y12 = right(x11,y11,T)
    ex,ey = right(x12,y12,F)
    return ex,ey

def J(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,F)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = left(x4,y4,F)
    x6,y6 = down(x5,y5,T)
    x7,y7 = down(x6,y6,T)
    x8,y8 = left(x7,y7,T)
    x9,y9 = right(x8,y8,F)
    x10,y10 = right(x9,y9,F)
    ex,ey = right(x10,y10,F)
    return ex,ey

def K(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = down(x2,y2,F)
    x4,y4 = right(x3,y3,T)
    x5,y5 = up_diag_l2r(x4,y4,T)
    x6,y6 = down(x5,y5,F)
    x7,y7 = down(x6,y6,F)
    x8,y8 = up_diag_r2l(x7,y7,T)
    x9,y9 = right(x8,y8,F)
    x10,y10 = right(x9,y9,F)
    ex,ey = down(x10,y10,F)
    return ex,ey

def L(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,F)
    x4,y4 = right(x3,y3,F)
    x5,y5 = down(x4,y4,F)
    x6,y6 = down(x5,y5,F)
    x7,y7 = left(x6,y6,F)
    x8,y8 = left(x7,y7,T)
    x9,y9 = right(x8,y8,F)
    x10,y10 = right(x9,y9,F)
    ex,ey = right(x10,y10,F)
    return ex,ey

def M(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = down_diag_l2r(x2,y2,T)
    x4,y4 = up_diag_l2r(x3,y3,T)
    x5,y5 = down(x4,y4,T)
    x6,y6 = down(x5,y5,T)
    ex,ey = right(x6,y6,F)
    return ex,ey

def N(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = down_diag_l2r(x2,y2,T)
    x4,y4 = down_diag_l2r(x3,y3,T)
    x5,y5 = up(x4,y4,T)
    x6,y6 = up(x5,y5,T)
    x7,y7 = down(x6,y6,F)
    x8,y8 = down(x7,y7,F)
    ex,ey = right(x8,y8,F)
    return ex,ey

def O(x, y):
    x1,y1 = up(x,y,F)
    x2,y2 = up_diag_l2r(x1,y1,T)
    x3,y3 = down_diag_l2r(x2,y2,T)
    x4,y4 = down_diag_r2l(x3,y3,T)
    x5,y5 = up_diag_r2l(x4,y4,T)
    x6,y6 = down(x5,y5,F)
    x7,y7 = right(x6,y6,F)
    x8,y8 = right(x7,y7,F)
    ex,ey = right(x8,y8,F)
    return ex,ey

def P(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,T)
    x6,y6 = left(x5,y5,T)
    x7,y7 = left(x6,y6,T)
    x8,y8 = down(x7,y7,F)
    x9,y9 = right(x8,y8,F)
    x10,y10 = right(x9,y9,F)
    ex,ey = right(x10,y10,F)
    return ex,ey

def Q(x, y):
    x1,y1 = up(x,y,F)
    x2,y2 = up_diag_l2r(x1,y1,T)
    x3,y3 = down_diag_l2r(x2,y2,T)
    x4,y4 = down_diag_r2l(x3,y3,T)
    x5,y5 = up_diag_r2l(x4,y4,T)
    x6,y6 = left(x5,y5,F)
    x7,y7 = down_diag_l2r(x6,y6,T)
    ex,ey = right(x7,y7,F)  
    return ex,ey

def R(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,T)
    x6,y6 = left(x5,y5,T)
    x7,y7 = left(x6,y6,T)
    x8,y8 = right(x7,y7,F)
    x9,y9 = down_diag_l2r(x8,y8,T)
    ex,ey = right(x9,y9,F)
    return ex,ey

def S(x, y):
    x1,y1 = up(x,y,F)
    x2,y2 = up(x1,y1,T)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down(x4,y4,F)
    x6,y6 = down(x5,y5,T)
    x7,y7 = up(x6,y6,F)
    x8,y8 = left(x7,y7,T)
    x9,y9 = left(x8,y8,T)
    x10,y10 = down(x9,y9,F)
    x11,y11 = right(x10,y10,T)
    x12,y12 = right(x11,y11,T)
    ex,ey = right(x12,y12,F)
    return ex,ey

def T(x, y):
    x1,y1 = right(x,y,F)
    x2,y2 = up(x1,y1,T)
    x3,y3 = up(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = left(x4,y4,F)
    x6,y6 = left(x5,y5,T)
    x7,y7 = down(x6,y6,F)
    x8,y8 = down(x7,y7,F)
    x9,y9 = right(x8,y8,F)
    x10,y10 = right(x9,y9,F)
    ex,ey = right(x10,y10,F)
    return ex,ey

def U(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = down(x2,y2,F)
    x4,y4 = down(x3,y3,F)
    x5,y5 = right(x4,y4,T)
    x6,y6 = right(x5,y5,T)
    x7,y7 = up(x6,y6,T)
    x8,y8 = up(x7,y7,T)
    x9,y9 = down(x8,y8,F)
    x10,y10 = down(x9,y9,F)
    ex,ey = right(x10,y10,F)
    return ex,ey

def V(x, y):
    x1,y1 = up(x,y,F)
    x2,y2 = up(x1,y1,T)
    x3,y3 = down(x2,y2,F)
    x4,y4 = down_diag_l2r(x3,y3,T)
    x5,y5 = up_diag_l2r(x4,y4,T)
    x6,y6 = up(x5,y5,T)
    x7,y7 = down(x6,y6,F)
    x8,y8 = down(x7,y7,F)
    ex,ey = right(x8,y8,F)
    return ex,ey 

def W(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = down(x2,y2,F)
    x4,y4 = down(x3,y3,F)
    x5,y5 = up_diag_l2r(x4,y4,T)
    x6,y6 = down_diag_l2r(x5,y5,T)
    x7,y7 = up(x6,y6,T)
    x8,y8 = up(x7,y7,T)
    x9,y9 = down(x8,y8,F)
    x10,y10 = down(x9,y9,F)
    ex,ey = right(x10,y10,F)
    return ex,ey

def X(x, y):
    x1,y1 = up_diag_l2r(x,y,T)
    x2,y2 = up_diag_l2r(x1,y1,T)
    x3,y3 = left(x2,y2,F)
    x4,y4 = left(x3,y3,F)
    x5,y5 = down_diag_l2r(x4,y4,T)
    x6,y6 = down_diag_l2r(x5,y5,T)
    ex,ey = right(x6,y6,F)
    return ex,ey

def Y(x, y):
    x1,y1 = up(x,y,F)
    x2,y2 = up(x1,y1,T)
    x3,y3 = down(x2,y2,F)
    x4,y4 = right(x3,y3,T)
    x5,y5 = right(x4,y4,T)
    x6,y6 = up(x5,y5,T)
    x7,y7 = down(x6,y6,F)
    x8,y8 = down(x7,y7,T)
    ex,ey = right(x8,y8,F)
    return ex,ey

def Z(x, y):
    x1,y1 = up(x,y,F)
    x2,y2 = up(x1,y1,F)
    x3,y3 = right(x2,y2,T)
    x4,y4 = right(x3,y3,T)
    x5,y5 = down_diag_r2l(x4,y4,T)
    x6,y6 = down_diag_r2l(x5,y5,T)
    x7,y7 = right(x6,y6,T)
    x8,y8 = right(x7,y7,T)
    ex,ey = right(x8,y8,F)
    return ex,ey

def execute_letters(letter, x, y):
    if letter == 'A':
        nx, ny = A(x,y)
        return nx, ny
    elif letter == 'B':
        nx, ny = B(x,y)
        return nx, ny
    elif letter == 'C':
        nx, ny = C(x,y)
        return nx, ny
    elif letter == 'D':
        nx, ny = D(x,y)
        return nx, ny
    elif letter == 'E':
        nx, ny = E(x,y)
        return nx, ny
    elif letter == 'F':
        nx, ny = F(x,y)
        return nx, ny
    elif letter == 'G':
        nx, ny = G(x,y)
        return nx, ny
    elif letter == 'H':
        nx, ny = H(x,y)
        return nx, ny
    elif letter == 'I':
        nx, ny = I(x,y)
        return nx, ny
    elif letter == 'J':
        nx, ny = J(x,y)
        return nx, ny
    elif letter == 'K':
        nx, ny = K(x,y)
        return nx, ny
    elif letter == 'L':
        nx, ny = L(x,y)
        return nx, ny
    elif letter == 'M':
        nx, ny = M(x,y)
        return nx, ny
    elif letter == 'N':
        nx, ny = N(x,y)
        return nx, ny
    elif letter == 'O':
        nx, ny = O(x,y)
        return nx, ny
    elif letter == 'P':
        nx, ny = P(x,y)
        return nx, ny
    elif letter == 'Q':
        nx, ny = Q(x,y)
        return nx, ny
    elif letter == 'R':
        nx, ny = R(x,y)
        return nx, ny
    elif letter == 'S':
        nx, ny = S(x,y)
        return nx, ny
    elif letter == 'T':
        nx, ny = T(x,y)
        return nx, ny
    elif letter == 'U':
        nx, ny = U(x,y)
        return nx, ny
    elif letter == 'V':
        nx, ny = V(x,y)
        return nx, ny
    elif letter == 'W':
        nx, ny = W(x,y)
        return nx, ny
    elif letter == 'X':
        nx, ny = X(x,y)
        return nx, ny
    elif letter == 'Y':
        nx, ny = Y(x,y)
        return nx, ny
    elif letter == 'Z':
        nx, ny = Z(x,y)
        return nx, ny

####################
## MAIN FUNCTIONS ##
####################
x1 = 0
y1 = 0
while True:

    letters = input("WHAT LETTERS DO YOU WANT (all caps please)?  ")
    for i in letters:
        nx, ny = execute_letters(i, x1, y1)
        x1 = nx
        y1 = ny