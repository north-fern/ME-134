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
shoulder = servo.Servo(pca.channels[3])
elbow= servo.Servo(pca.channels[6])
pen = servo.Servo(pca.channels[9])
 
#setting lengths for arms
length1 = 1
length2 = 2

#setting unit step of letters
unitstep = 1

#setting up button
#https://raspberrypihq.com/use-a-push-button-with-raspberry-pi-gpio/
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#set to pin 10 - connect from pin 10 to 3.3 power w/ resistor

#######################
## FIND MOTOR ANGLES ##
#######################
def theta1, theta2 = getAngles(x,y)
    theta2 = math.acos(((x^2) + (y^2) - (length1^2) - (length2^2)/(2*length2*length1)))
    a = length1 + length2*cos(theta2)
    b = length2*sin(theta1)*((x + length2*sin(theta2))/(length1 + length2*cos(theat2)))
    theta1 = math.asin(y/(a*b))
    return theta1, theta2

#####################
## PEN DEFINITIONS ##
#####################
def pen_up():
    i = 0
    while GPIO.input(10) != GPIO.HIGH:
        pen.angle() = i+1
        i = i + 1
    
def pen_down():
        i = 50
    while GPIO.input(10) != GPIO.HIGH:
        pen.angle() = i-1
        i = i - 1

######################
## MOTION FUNCTIONS ##
######################
def nx,ny = up(x, y, WRITE_BOOL):
    
    nx = x
    ny = y + unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    elbow.angle = an2
    return nx,ny

def nx,ny = down(x, y, WRITE_BOOL):
     
    nx = x
    ny = y - unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    elbow.angle = an2
    return nx,ny

def nx,ny = left(x, y, WRITE_BOOL):
    
    nx = x - unitstep
    ny = y 
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    elbow.angle = an2
    return nx,ny

def nx,ny = right(x, y, WRITE_BOOL):
    
    nx = x + unitstep
    ny = y 
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    elbow.angle = an2
    return nx,ny

def nx,ny = down_diag_l2r(x, y, WRITE_BOOL):
    
    nx = x + unitstep
    ny = y - unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    elbow.angle = an2
    return nx,ny

def nx,ny = down_diag_r2l(x, y, WRITE_BOOL):
    
    nx = x - unitstep
    ny = y - unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    elbow.angle = an2
    return nx,ny

def nx,ny = up_diag_l2r(x, y, WRITE_BOOL):
    
    nx = x + unitstep
    ny = y + unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    elbow.angle = an2
    return nx,ny

def nx,ny = up_diag_r2l(x, y, WRITE_BOOL):
    
    nx = x - unitstep
    ny = y + unitstep
    an1, an2 = getAngles(nx,ny)
    
    if WRITE_BOOL == 'T':
        pen_down()
    else:
        pen_up()
    shoulder.angle = an1
    elbow.angle = an2
    return nx,ny

#######################
## LETTER DEFINITONS ##
#######################
def ex,ey = A(x, y):
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
    return ex,ey

def ex,ey = B(x, y):
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

def ex,ey = C(x, y):
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

def ex,ey = E(x, y):
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

def ex,ey = F(x, y):
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

def ex,ey = G(x, y):
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

def ex,ey = H(x, y):
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

def ex,ey = I(x, y):
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

def ex,ey = J(x, y):
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

def ex,ey = K(x, y):
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

def ex,ey = L(x, y):
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

def ex,ey = M(x, y):
    x1,y1 = up(x,y,T)
    x2,y2 = up(x1,y1,T)
    x3,y3 = down_diag_l2r(x2,y2,T)
    x4,y4 = up_diag_l2r(x3,y3,T)
    x5,y5 = down(x4,y4,T)
    x6,y6 = down(x5,y5,T)
    ex,ey = right(x6,y6,F)
    return ex,ey

def ex,ey = N(x, y):
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

def ex,ey = O(x, y):
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

def ex,ey = P(x, y):
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

def ex,ey = Q(x, y):
    x1,y1 = up(x,y,F)
    x2,y2 = up_diag_l2r(x1,y1,T)
    x3,y3 = down_diag_l2r(x2,y2,T)
    x4,y4 = down_diag_r2l(x3,y3,T)
    x5,y5 = up_diag_r2l(x4,y4,T)
    x6,y6 = left(x5,y5,F)
    x7,y7 = down_diag_l2r(x6,y6,T)
    ex,ey = right(x7,y7,F)  
    return ex,ey

def ex,ey = R(x, y):
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

def ex,ey = S(x, y):
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

def ex,ey = T(x, y):
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

def ex,ey = U(x, y):
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

def ex,ey = V(x, y):
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

def ex,ey = W(x, y):
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

def ex,ey = X(x, y):
    x1,y1 = up_diag_l2r(x,y,T)
    x2,y2 = up_diag_l2r(x1,y1,T)
    x3,y3 = left(x2,y2,F)
    x4,y4 = left(x3,y3,F)
    x5,y5 = down_diag_l2r(x4,y4,T)
    x6,y6 = down_diag_l2r(x5,y5,T)
    ex,ey = right(x6,y6,F)
    return ex,ey

def ex,ey = Y(x, y):
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

def ex,ey = Z(x, y):
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

def nx, ny = execute_letters(letter, x, y):
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

while True:
    x = 0
    y = 0
    letters = input("WHAT LETTERS DO YOU WANT (all caps please)?  ")
    for i in length(letters):
        nx, ny = execute_letter(letters[i], x, y)
        x = nx
        y = ny