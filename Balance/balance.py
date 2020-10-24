import FaBo9Axis_MPU9250 
import time
import sys
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import random2 as random
from adafruit_motor  import servo
import os
import smbus

from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()
imu.readSensor()
imu.computeOrientation()
goal_x = imu.roll
goal_y = imu.pitch

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50


## servo setup

s1 = servo.Servo(pca.channels[0])
s2 = servo.Servo(pca.channels[3])
s3 = servo.Servo(pca.channels[6])

s1_curt_ang = 0
s2_curt_ang = 0
s3_curt_ang = 0


while True:
    motor = random.randrange(0,2,1)
    angleDelta = random.randrange(-5, 5, 1)
    imu.readSensor()
    imu.computeOrientation()
    pre_diff_pitch = 100
    pre_diff_roll = 100
    if motor == 0:
        if (s1_curt_ang + angleDelta) >= 0 and (s1_curt_ang + angleDelta)  <= 180:
            s1.angle = s1_curt_ang + angleDelta
            if abs(imu.roll - goal_x) < pre_diff_pitch or abs(imu.roll - goal_y) < pre_diff_roll:
                pre_diff_pitch = abs(imu.pitch - goal_x)
                pre_diff_roll = abs(imu.roll - goal_y)
                s1_curt_ang = s1_curt_ang + angleDelta
            else:
                s1.angle = s1_curt_ang
        else:
            s1.angle = s1_curt_ang
    if motor == 1:
        if (s2_curt_ang + angleDelta) >= 0 and (s2_curt_ang + angleDelta)  <= 180:
            s2.angle = s2_curt_ang + angleDelta
            if abs(imu.pitch - goal_x) < pre_diff_pitch or abs(imu.roll - goal_y) < pre_diff_roll:
                pre_diff_pitch = abs(imu.pitch - goal_x)
                pre_diff_roll = abs(imu.roll - goal_y)
                s1_curt_ang = s2_curt_ang + angleDelta
            else:
                s2.angle = s2_curt_ang
        else:
            s2.angle = s2_curt_ang
    if motor == 2:
        if (s3_curt_ang + angleDelta) >= 0 and (s3_curt_ang + angleDelta)  <= 180:
            s3.angle = s3_curt_ang + angleDelta
            if abs(imu.pitch - goal_x) < pre_diff_pitch or abs(imu.roll - goal_y) < pre_diff_roll:
                pre_diff_pitch = abs(imu.pitch - goal_x)
                pre_diff_roll = abs(imu.roll - goal_y)
                s1_curt_ang = s3_curt_ang + angleDelta
            else:
                s3.angle = s3_curt_ang
        else:
            s3.angle = s3_curt_ang
