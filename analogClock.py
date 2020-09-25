#https://github.com/adafruit/Adafruit_CircuitPython_PCA9685/blob/master/examples/pca9685_servo.py
#basic form from here ^^

import time
from adafruit_motor import servo
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

#setting up I2C communication
i2c_bus  = busio.I2C(SCL, SDA)
pca = PCA9685(i2c_bus)
pca.frequency = 50

#creating the servos - CHECK CHANNELS AND CONFIRM
hourServo = servo.Servo(pca.channels[3])
minuteServo = servo.Servo(pca.channels[6])

######################
#function definitions#
######################
def set_hour_servo(hour, minute):
    print("Doing Something HOURS")
    if hour > 12:
        hourNEW = hour%12
        hour = hourNEW
        print(hour)

    if minute < 12:
        angle = ((hour-1)*15 + 0)
        hourServo.angle = (angle)
        print(angle)
    if minute < 24:
        angle = ((hour-1)*15 + 3)
        hourServo.angle = (angle)
        print(angle)
    if minute < 36:
        angle = ((hour-1)*15 + 6)
        hourServo.angle = (angle)
        print(angle)
    if minute < 48:
        angle = ((hour-1)*15 + 9)
        hourServo.angle = (angle)
        print(angle)
    if minute < 60:
        angle = ((hour-1)*15 + 12)
        hourServo.angle = (angle)
        print(angle)

def set_minute_servo(minute):
    print("Doing Something Else MINUTES")
    angle = minute*3
    minuteServo.angle = (angle)
    print(angle)


hourServo.angle = (0)
minuteServo.angle = (0)
###########
#code body#
###########

while True:
    timeNOW = time.localtime()
    hour = timeNOW.tm_hour
    minute = timeNOW.tm_min
    print(hour + minute)
    set_hour_servo(hour, minute)
    set_minute_servo(minute)
    time.sleep(10)




#ENDING I2C Connection!
pca.deinit()