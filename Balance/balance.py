'''
This code is designe for a balancing robot. The three servos are placed in 120* separations from each other
around the edge of a styrofoam ball. They move randomly and check to see if they are closer to being balanced. 
The IMU is placed in the center of the ball and the program (imusensor library) calculates a roll, pitch and yaw.
If the pi senses that the difference between the goal points and new points is better, it keeps the new motor angl$
if it isn't it goes back to the previous angle. The angle additon is randomly generated. 
'''


'''
Imports
'''
import FaBo9Axis_MPU9250 
import time
import sys
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import random
from adafruit_motor  import servo
import os
import smbus
from imusensor.MPU9250 import MPU9250


'''
setup of IMU and begining calculations
'''
address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()
imu.readSensor()
imu.computeOrientation()
goal_x = imu.roll
goal_y = imu.pitch

print("Goal vals are" + str(goal_y) + "  " + str(goal_y))

'''
setting up motor driver
'''
i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50


'''
servo setup
'''
s1 = servo.Servo(pca.channels[0])
s2 = servo.Servo(pca.channels[3])
s3 = servo.Servo(pca.channels[6])

'''
initialize current angles of servo
'''
s1_curt_ang = 0
s2_curt_ang = 0
s3_curt_ang = 0
ang = 30
k = 1
val = True

pre_diff_roll = 1000
pre_diff_pitch = 1000

while val == True:

    ##randomly choose motor
    motor = random.randint(0,2)
    print("Random motor choice is :" + str(motor))
    print("Error Roll: " + str(pre_diff_roll) + " Error Pitch: " + str(pre_diff_pitch))
    ## randomly choose angle to change by
    angleDelta = random.randint(-k*ang, k*ang)
    imu.readSensor()
    imu.computeOrientation()
    print("M1: " + str(s1_curt_ang) + " M2: " + str(s2_curt_ang) + " M3: " + str(s3_curt_ang))

    ##set initial differences, make them large
    if pre_diff_pitch < 10 and pre_diff_roll < 10:
         k = .8
    elif pre_diff_pitch < 5 and pre_diff_roll < 5:
         k = .6

     ## setup of motor selection
    if motor == 0:
        if (s1_curt_ang + angleDelta) >= 0 and (s1_curt_ang + angleDelta)  <= 180:
            # check to see if angle is out of range
            s1.angle = s1_curt_ang + angleDelta
            time.sleep(.1)
            imu.readSensor()
            imu.computeOrientation()
            if abs(imu.roll - goal_x) < pre_diff_pitch or abs(imu.roll - goal_y) < pre_diff_roll:
                #check to see if new value is better; if it is, change baselines
                pre_diff_pitch = abs(imu.pitch - goal_x)
                pre_diff_roll = abs(imu.roll - goal_y)
                s1_curt_ang = s1_curt_ang + angleDelta
            else:
                s1.angle = s1_curt_ang
                time.sleep(.1)
        else:
            s1.angle = s1_curt_ang
            time.sleep(.1)
    
    if motor == 1:
        if (s2_curt_ang + angleDelta) >= 0 and (s2_curt_ang + angleDelta)  <= 180:
            # check to see if angle is out of range
            s2.angle = s2_curt_ang + angleDelta
            time.sleep(.1)
            imu.readSensor()
            imu.computeOrientation()
            if abs(imu.pitch - goal_x) < pre_diff_pitch or abs(imu.roll - goal_y) < pre_diff_roll:
                #check to see if new value is better; if it is, change baselines
                pre_diff_pitch = abs(imu.pitch - goal_x)
                pre_diff_roll = abs(imu.roll - goal_y)
                s1_curt_ang = s2_curt_ang + angleDelta
            else:
                s2.angle = s2_curt_ang
                time.sleep(.1)
        else:
            s2.angle = s2_curt_ang
            time.sleep(.1)

    if motor == 2:
        if (s3_curt_ang + angleDelta) >= 0 and (s3_curt_ang + angleDelta)  <= 180:
            # check to see if angle is out of range
            s3.angle = s3_curt_ang + angleDelta
            time.sleep(.1)
            imu.readSensor()
            imu.computeOrientation()
            if abs(imu.pitch - goal_x) < pre_diff_pitch or abs(imu.roll - goal_y) < pre_diff_roll:
                #check to see if new value is better; if it is, change baselines
                pre_diff_pitch = abs(imu.pitch - goal_x)
                pre_diff_roll = abs(imu.roll - goal_y)
                s1_curt_ang = s3_curt_ang + angleDelta
            else:
                s3.angle = s3_curt_ang
                time.sleep(.1)
        else:
            s3.angle = s3_curt_ang
            time.sleep(.1)

    if pre_diff_roll < 0 and pre_diff_pitch < 2:
        time.sleep(30)
        val = False

