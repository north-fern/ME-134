
from __future__ import division

import time
#import board
from board import SCL, SDA
#import picamera
#import numpy as np
import io
import pulseio
from adafruit_motor import servo
import busio
from adafruit_pca9685 import PCA9685
from pynput.keyboard import Listener
from pynput import keyboard

width = 100
height = 100

# create a PWMOut object on the control pin.
i2c = busio.I2C(SCL, SDA)
#stream = io.BytesIO()

#create pwm object with 50hz frequency
pca = PCA9685(i2c)
pca.frequency = 50

#Set up servos
hammerServo = servo.Servo(pca.channels[0], min_pulse=400, max_pulse=2400)
sweepServo = servo.Servo(pca.channels[1], min_pulse=400, max_pulse=2400)
sweepServoAngle = 90
sweepServo.angle = sweepServoAngle
hammerServoAngle = 90
hammerServo.angle = hammerServoAngle

#class MyAnalysis(picamera.array.PiRGBAnalysis):
#    def __init__(self, camera):
#        super(MyAnalysis, self).__init__(camera)
#        self.frame_num = 0

#    def analyse(self, a):
#        r = int(np.mean(a[..., 0]))
#        g = int(np.mean(a[..., 1]))
#        b = int(np.mean(a[..., 2]))
#        c = (r << 16) | (g << 8) | b
#        print('Average color: #%06x' % c)
#        self.frame_num += 1

def on_press(key):
    print("Key pressed: {0}".format(key))
    if (key == keyboard.Key.up):
        MoveForward()
    if (key == keyboard.Key.left):
        TurnLeft()
    if (key == keyboard.Key.right):
        TurnRight()
    
def on_release(key):
    print("Key released: {0}".format(key))

def MoveForward():
    if (sweepServoAngle <= 90):
        ResetArm()
        SweepArm('left')
    elif (sweepServoAngle > 90):
        ResetArm()
        SweepArm('right')

def TurnRight():
    ResetArm()
    SweepArm('left')

def TurnLeft():
    ResetArm()
    SweepArm('right')
        
def ResetArm():
    global hammerServoAngle, sweepServoAngle
    while (hammerServoAngle > 90):
        hammerServoAngle = hammerServoAngle - 1
        hammerServo.angle = hammerServoAngle
        print("HammerArm:" + str(hammerServoAngle))
        time.sleep(0.05)

    while(sweepServoAngle < 90):
        sweepServoAngle = sweepServoAngle + 1
        sweepServo.angle = sweepServoAngle
        print("SweepArm:" + str(sweepServoAngle))
        time.sleep(0.05)

    while(sweepServoAngle > 90):
        sweepServoAngle = sweepServoAngle - 1
        sweepServo.angle = sweepServoAngle
        print("SweepArm:" + str(sweepServoAngle))
        time.sleep(0.05)


def SweepArm(direction):
    global hammerServoAngle, sweepServoAngle
    if (direction == 'right'):
        hammerServoAngle = 180
        hammerServo.angle = hammerServoAngle
        while(sweepServoAngle > 5):
            sweepServoAngle = sweepServoAngle-1
            sweepServo.angle = sweepServoAngle
            print("SweepArm:" + str(sweepServoAngle))
            time.sleep(0.03)

    if (direction == 'left'):
        hammerServoAngle = 180
        hammerServo.angle = hammerServoAngle
        while(sweepServoAngle < 175):
            sweepServoAngle = sweepServoAngle+1
            sweepServo.angle = sweepServoAngle
            print("SweepArm:" + str(sweepServoAngle))
            time.sleep(0.03)
        

def GetSightInRgb():
    pass
#    with picamera.PiCamera() as camera:
#        camera.resolution = (width, height)
#        output = MyAnalysis(camera)
#        image = np.empty((128, 112, 3), dtype=np.uint8)
#        camera.capture(image, 'rgb')
#        image = image[:100, :100]

def DetectLine():
    pass
    #RGBView = GetSightInRgb()
    #print()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

while (True):
    time.sleep(0.1)
    #DetectLine()

pca.deinit()