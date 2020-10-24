from fusion import Fusion
import FaBo9Axis_MPU9250 
import time
import sys
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import random2
from adafruit_motor  import servo

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50

ImU = FaBo9Axis_MPU9250.MPU9250()
fuse = Fusion()

## servo setup

s1 = servo.Servo(pca.channels[0])
s2 = servo.Servo(pca.channels[3])
s3 = servo.Servo(pca.channels[6])

s1_curt_ang = 0
s2_curt_ang = 0
s3_curt_ang = 0

## setup fuse 
acel = ImU.readAccel()
gyr = ImU.readGyro()
mag = IMU.readMagnet()
fuse.update(accel, gyro, mag)
goal_x = fuse.pitch
goal_y = fuse.roll


def update_vals():
    acel = ImU.readAccel()
    gyr = ImU.readGyro()
    mag = IMU.readMagnet()
    fuse.update(accel, gyro, mag)



while True:
    motor = random.randrange(0,2,1)
    angleDelta = random.randrange(-5, 5, 1)
    pre_diff_pitch = 100
    pre_diff_roll = 100
    if motor == 0:
        s1.angle = s1_curt_ang + angleDelta
        if abs(fuse.pitch - goal_x) < pre_diff_pitch or abs(fuse.roll - goal_y) < pre_diff_roll:
            pre_diff_pitch = abs(fuse.pitch - goal_x)
            pre_diff_roll = abs(fuse.roll - goal_y)
            s1_curt_ang = s1_curt_ang + angleDelta
        else:
            s1.angle = s1_curt_ang
    if motor == 1:
        s2.angle = s2_curt_ang + angleDelta
        if abs(fuse.pitch - goal_x) < pre_diff_pitch or abs(fuse.roll - goal_y) < pre_diff_roll:
            pre_diff_pitch = abs(fuse.pitch - goal_x)
            pre_diff_roll = abs(fuse.roll - goal_y)
            s1_curt_ang = s2_curt_ang + angleDelta
        else:
            s2.angle = s2_curt_ang
    if motor == 2:
        s3.angle = s3_curt_ang + angleDelta
        if abs(fuse.pitch - goal_x) < pre_diff_pitch or abs(fuse.roll - goal_y) < pre_diff_roll:
            pre_diff_pitch = abs(fuse.pitch - goal_x)
            pre_diff_roll = abs(fuse.roll - goal_y)
            s1_curt_ang = s3_curt_ang + angleDelta
        else:
            s3.angle = s3_curt_ang
