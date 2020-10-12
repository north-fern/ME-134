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
a1 = 5.07
a2 = 6
wait_time = .2

#setting unit step of letters
unitstep = .25

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
    t1 = math.pi/2 - math.atan2( (a1**3*x + a1*x*(-a2**2 + x**2 + y**2) + \
     math.sqrt(-(a1**2*y**2*(a1**4 + (-a2**2 + x**2 + y**2)**2 - \
     2*a1**2*(a2**2 + x**2 + y**2)))))/(a1**2*(x**2 + y**2)),\
     (a1**3*y**2 + a1*y**2*(-a2**2 + x**2 + y**2) - \
     x*math.sqrt(-(a1**2*y**2*(a1**4 + (-a2**2 + x**2 + y**2)**2 -\
     2*a1**2*(a2**2 + x**2 + y**2)))))/(a1**2*y*(x**2 + y**2)))

    t2 = math.acos((x**2 + y**2 - a1**2 - a2**2)/(2 * a1 * a2))

    t11 = t1 * 180/3.141592
    t1 = t11*(-2/3) + 120
    t22 = t2 * 180/3.141592
    t2 = t22*(18/13)
    return t1, t2


def move_slow_S(pastAng, curr_ang):
    ang = pastAng
    if pastAng < curr_ang:
        while ang < curr_ang:
            ang = ang + 2
            shoulder.angle = ang
            time.sleep(.1)
    else:
        while ang > curr_ang:
            ang = ang - 2
            shoulder.angle = ang
            time.sleep(.1)

def move_slow_E(pastAng, curr_ang):
    ang = pastAng
    if pastAng < curr_ang:
        while ang < curr_ang:
            ang = ang + 2
            elbow.angle = ang
            time.sleep(.1)
    else:
        while ang > curr_ang:
            ang = ang - 2
            elbow.angle = ang
            time.sleep(.1)



######################
## MOTION FUNCTIONS ##
######################
def up(x, y, olda, oldb):
    nx = x
    ny = y + unitstep
    an1, an2 = getAngles(nx,ny)
    
    move_slow_E(oldb, an2)
    move_slow_S(olda, an1)
    print(str(nx) + "," + str(ny))
    return nx,ny, an1, an2

def down(x, y, olda, oldb):
     
    nx = x
    ny = y - unitstep
    an1, an2 = getAngles(nx,ny)
    
    
    move_slow_E(oldb, an2)
    move_slow_S(olda, an1)
    print(str(nx) + "," + str(ny))
    return nx,ny, an1, an2


def left(x, y, olda, oldb):
    
    nx = x - unitstep
    ny = y 
    an1, an2 = getAngles(nx,ny)
    
    move_slow_E(oldb, an2)
    move_slow_S(olda, an1)
    print(str(nx) + "," + str(ny))
    return nx,ny, an1, an2


def right(x, y, olda, oldb):
    
    nx = x + unitstep
    ny = y 
    an1, an2 = getAngles(nx,ny)
    
    
    move_slow_E(oldb, an2)
    move_slow_S(olda, an1)
    print(str(nx) + "," + str(ny))
    return nx,ny, an1, an2

def down_diag_l2r(x, y, olda, oldb):
    
    nx = x + unitstep
    ny = y - unitstep
    an1, an2 = getAngles(nx,ny)
    
    
    move_slow_E(oldb, an2)
    move_slow_S(olda, an1)
    print(str(nx) + "," + str(ny))
    return nx,ny, an1, an2

def down_diag_r2l(x, y, olda, oldb):
    
    nx = x - unitstep
    ny = y - unitstep
    an1, an2 = getAngles(nx,ny)
    
    
    move_slow_E(oldb, an2)
    move_slow_S(olda, an1)
    print(str(nx) + "," + str(ny))
    return nx,ny, an1, an2

def up_diag_l2r(x, y, olda, oldb):
    
    nx = x + unitstep
    ny = y + unitstep
    an1, an2 = getAngles(nx,ny)
    
    
    move_slow_E(oldb, an2)
    move_slow_S(olda, an1)
    print(str(nx) + "," + str(ny))
    return nx,ny, an1, an2

def up_diag_r2l(x, y, olda, oldb):
    
    nx = x - unitstep
    ny = y + unitstep
    an1, an2 = getAngles(nx,ny)
    
    
    move_slow_E(oldb, an2)
    move_slow_S(olda, an1)
    print(str(nx) + "," + str(ny))
    return nx,ny, an1, an2

#######################
## LETTER DEFINITONS ##
#######################
'''
def A(x, y):
    
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
    
    ex,ey = up(0,0,T)
    return ex,ey

def B(x, y, a, b):
    x1,y1,a1,a2 = up(x,y,a, b)
    x2,y2,a1,a2= up(x1,y1,a1, a2)
    x3,y3,a1,a2 = right(x2,y2,T)
    x4,y4,a1,a2 = right(x3,y3,T)
    x5,y5,a1,a2 = down(x4,y4,T)
    x6,y6,a1,a2 = down(x5,y5,T)
    x7,y7,a1,a2 = up(x6,y6,F)
    x8,y8,a1,a2 = left(x7,y7,T)
    x9,y9,a1,a2 = left(x8,y8,T)
    x10,y10,a1,a2 = down(x9,y9,F)
    x11,y11,a1,a2 = right(x10,y10,T)
    x12,y12,a1,a2 = right(x11,y11,T)
    ex,ey,a1,a2 = right(x12,y12,F)
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
'''
def K(x, y, a, b):
    x1, y1, a1, b1 = up(x,y,a, b)
    x2,y2, a1, b1 = up(x1,y1, a1, b1)
    x3,y3, a1, b1 = down(x2,y2, a1, b1)
    x4,y4, a1, b1 = right(x3,y3, a1, b1)
    x5,y5, a1, b1 = up_diag_l2r(x4,y4, a1, b1)
    x6,y6, a1, b1 = down(x5,y5, a1, b1)
    x7,y7, a1, b1 = down(x6,y6, a1, b1)
    x8,y8, a1, b1 = up_diag_r2l(x7,y7, a1, b1)
    x9,y9, a1, b1 = right(x8,y8, a1, b1)
    x10,y10, a1, b1 = right(x9,y9, a1, b1)
    ex,ey, a, b = down(x10,y10, a1, b1)
    return ex,ey, a, b
'''
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
'''
def M(x, y, a, b):
    x1, y1, a1, b1 = up(x,y,a, b)
    x2, y2, a2, b2 = up(x1, y1, a1, b1)
    x3,y3, a3, b3 = up(x2, y2, a2, b2)
    x4,y4, a4, b4 = up(x3,y3, a3, b3)
    x5,y5,a5, b5 = up(x4,y4, a4, b4)
    x6,y6,a6, b6 = up(x5,y5,a5, b5)
    x7,y7,a7, b7 = up(x6,y6,a6, b6)
    x8,y8,a8, b8 = up(x7,y7,a7, b7 )
    x9,y9,a9, b9 = down_diag_l2r(x8,y8,a8, b8)
    x10,y10,a10, b10 = down_diag_l2r(x9,y9,a9, b9 )
    x11,y11,a11, b11 = down_diag_l2r(x10,y10,a10, b10)
    x12,y12,a12, b12 = down_diag_l2r(x11,y11,a11, b11)
    x13,y13,a13, b13 = up_diag_l2r(x12,y12,a12, b12)
    x14,y14,a14, b14 = up_diag_l2r( x13,y13,a13, b13)
    x15,y15,a15, b15 = up_diag_l2r(x14,y14,a14, b14)
    x16,y16,a16, b16 = up_diag_l2r(x15,y15,a15, b15)
    x17,y17,a17, b17 = down(x16,y16,a16, b16)
    x18,y18,a18, b18 = down(x17,y17,a17, b17)
    x19,y19,a19, b19 = down(x18,y18,a18, b18 )
    x20,y20,a20, b20 = down(x19,y19,a19, b19)
    x21,y21,a21, b21 = down(x20,y20,a20, b20)
    x22,y22,a22, b22 = down(x21,y21,a21, b21)
    x23,y23,a23, b23 = down(x22,y22,a22, b22)
    x24,y24,a24, b24 = down(x23,y23,a23, b23)
    x25,y25,a25, b25 = right(x24,y24,a24, b24)
    x26,y26,a26, b26 = right(x25,y25,a25, b25)
    x27,y27,a27, b27 = right(x26,y26,a26, b26)
    ex,ey,a, b = right(e27,e27,a27, b27)
    return ex,ey, a, b
'''
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
'''
def O(x, y, a, b):
    x1,y1 , a1, b1 = up(x,y,a, b)
    x2,y2 , a2, b2 = up(x1,y1,a1, b1)
    x3,y3 , a3, b3 = up(x2,y2 , a2, b2 )
    x4,y4 , a4, b4 = up(x3,y3 , a3, b3)
    x5,y5, a5, b5 = up_diag_l2r(x4,y4 , a4, b4  )
    x6,y6, a6, b6 = up_diag_l2r(x5,y5, a5, b5)
    x7,y7, a7, b7= up_diag_l2r(x6,y6, a6, b6 )
    x8,y8, a8, b8 = up_diag_l2r(x7,y7, a7, b7)
    x9,y9, a9, b9 = down_diag_l2r(x8,y8, a8, b8)
    x10,y10, a10, b10 = down_diag_l2r(x9,y9, a9, b9)
    x11,y11, a11, b11 = down_diag_l2r(x10,y10, a10, b10)
    x12,y12, a12, b12 = down_diag_l2r(x11,y11, a11, b11)
    x13,y13, a13, b13 = down_diag_r2l(x12,y12, a12, b12)
    x14,y14, a14, b14 = up_diag_r2l(x13,y13, a13, b13)
    x15,y15, a15, b15 = up_diag_r2l(x14,y14, a14, b14)
    x16,y16, a16, b16 = up_diag_r2l(x15,y15, a15, b15)
    x17,y17, a17, b17 = up_diag_r2l( x16,y16, a16, b16)
    x18,y18, a18, b18 = down(x17,y17, a17, b17)
    x19,y19, a19, b19 = down(x18,y18, a18, b18 )
    x20,y20, a20, b20 = down(x19,y19, a19, b19)
    x21,y21, a21, b21 = down(x20,y20, a20, b20)
    x22,y22, a22, b22 = right(x21,y21, a21, b21)
    x23,y23, a23, b23 = right(x22,y22, a22, b22 )
    x24,y24, a24, b24 = right(x23,y23, a23, b23 )
    x25,y25, a25, b25 = right(x24,y24, a24, b24)
    x26,y26, a26, b26 = right(x25,y25, a25, b25 )
    x27,y27, a27, b27 = right(x26,y26, a26, b26)
    x28,y28, a28, b28 = right(x27,y27, a27, b27)
    x29,y29, a29, b29 = right(x28,y28, a28, b28)
    ex,ey, a, b = right(x29,y29, a29, b29)
    return ex,ey, a, b
'''
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
'''
def S(x, y, a, b):
    x1,y1,a1, b1 = up(x,y,a, b)
    x2,y2,a1, b1 = up(x1,y1,a1, b1)
    x3,y3,a1, b1 = right(x2,y2,a1, b1)
    x4,y4,a1, b1 = right(x3,y3,a1, b1)
    x5,y1, a1, b1 = down(x4,y4,a1, b1)
    x6,y6,a1, b1 = down(x5,y5,a1, b1)
    x7,y7,a1, b1 = up(x6,y6,a1, b1)
    x8,y8,a1, b1 = left(x7,y7,a1, b1)
    x9,y9,a1, b1 = left(x8,y8,a1, b1)
    x10,y10,a1, b1 = down(x9,y9,a1, b1)
    x11,y11,a1, b1 = right(x10,y10,a1, b1)
    x12,y12,a, b = right(x11,y11,a1, b1)
    ex,ey = right(x12,y12,F)
    return ex,ey
'''
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
'''
def execute_letters(letter, x, y, a, b):
    if letter == 'K':
        nx, ny, na, nb = K(x,y, a, b)
        return nx, ny, na, nb
    elif letter == 'M':
        nx, ny, na, nb = M(x,y, a, b)
        return nx, ny, na, nb
    elif letter == 'O':
        nx, ny, na, nb = O(x,y, a, b)
        return nx, ny, na, nb
    elif letter == 'S':
        nx, ny, na, nb = S(x,y, a, b)
        return nx, ny, na, nb
    else:
        print("ERROR")

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
a = 120
b = 90



x = int(input("starting x coordinate? "))
y = int(input("starting y coordinate?"))


shoulder.angle = a
elbow.angle = b
input("READY?")

x, y, a, b = execute_letters('O', x, y, a, b)
time.sleep(.25)
input("WAIT")
x = int(input("starting x coordinate? "))
y = int(input("starting y coordinate?"))

x, y, a, b = execute_letters('M', x, y, a, b)
time.sleep(.25)
input("DONE")

