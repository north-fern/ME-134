import time
from adafruit_motor import servo
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

i2c_bus  = busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus)

pca.frequency = 50
side = servo.Servo(pca.channels[0])
updown = servo.Servo(pca.channels[3])

side.angle = 180
updown.angle = 0

input()

def left():
    for i in range(90):
        side.angle = 180-i
        updown.angle = 0
    updown.angle = 30

def right():
    for j in range(90):
        side.angle = j
        updown.angle = 0
    updown.angle = 30


while True:
    left()
    side.angle = 75
    time.sleep(.1)
    side.angle = 55
    time.sleep(.1)
    side.angle = 35
    time.sleep(.1)
    side.angle = 0
    time.sleep(.1)
    side.angle = 0
    time.sleep(.1)
    right()
    '''
    side.angle = 0
    time.sleep(.1)
    side.angle = 0
    time.sleep(.1)
    side.angle = 35
    time.sleep(.1)
    side.angle = 55
    time.sleep(.1)
    side.angle = 75
    time.sleep(.1)
    '''

pca.deinit()

