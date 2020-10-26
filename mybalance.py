import FaBo9Axis_MPU9250 
from time import sleep
import sys
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
import random
from adafruit_motor  import servo
import os
import smbus
from imusensor.MPU9250 import MPU9250



#setup of IMU and begining calculations

address = 0x68
bus = smbus.SMBus(1)
imu = MPU9250.MPU9250(bus, address)
imu.begin()
#imu.readSensor()
#imu.computeOrientation()
goal_roll = 0
goal_pitch = 0

sleep(1)
print("Goal vals are " + str(goal_roll) + "  " + str(goal_pitch))

#setting up motor driver

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50



#servo setup

s1 = servo.Servo(pca.channels[0])
s2 = servo.Servo(pca.channels[3])
s3 = servo.Servo(pca.channels[6])


#initialize current angles of servo

s1_init_ang = 90
s2_init_ang = 90
s3_init_ang = 90

s1.angle = s1_init_ang
s2.angle = s2_init_ang
s3.angle = s3_init_ang

val =True
#upper limit change for servo
upper_limit_r = 0
upper_limit_p = 0


while val == True:
    imu.readSensor()
    imu.computeOrientation()
    #get the current angle
    currentroll = imu.roll
    currentpitch = imu.pitch
    diff_roll = abs(currentroll-goal_roll)
    diff_pitch = abs(currentpitch-goal_pitch)
    #if the error is greater than 5, keep servos on 
    if diff_roll > 10:
        #if the semiball goes to left, then weight(roll) goes to right(90--180)
        #if the semiball goes to right, then weight(roll) goes to left(10--90)
        if currentroll > 0:
            s1.angle = random.randint(90,180-upper_limit_r)
            sleep(1)
        else:
            s1.angle = random.randint(60,90-upper_limit_r)
            sleep(1)
        #after the first balancing, if things get better(i.e. the new angle smaller than current angle), decrease the upper limit by 5 degrees    
        imu.readSensor()
        imu.computeOrientation()
        newroll = imu.roll
        if abs(newroll) < abs(currentroll):
            upper_limit_r += 5
    
    if diff_pitch > 10:
        if currentpitch > 0:
            s2.angle = random.randint(90,135-upper_limit_p)
            sleep(1)
            s3.angle = random.randint(0,45-upper_limit_p)
            sleep(1)
        else:
            s2.angle = random.randint(0,45-upper_limit_p)
            sleep(1)
            s3.angle = random.randint(90,135-upper_limit_p)
            sleep(1)
            
        imu.readSensor()
        imu.computeOrientation()
        newpitch = imu.pitch
        if abs(newpitch) < abs(currentpitch):
            upper_limit_p += 5
           
    if diff_roll <= 10 and diff_pitch <= 10:
        print('diff_roll = ' + str(diff_roll) + ' diff_pitch = ' + str(diff_pitch))
        sleep(30)
        val = False
        
s1.angle = 90
s2.angle = 90
s3.angle = 90