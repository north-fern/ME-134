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
    print("Doing Something")
    if minute < 12:
        hourServo.angle((hour-1)*15 + 0)
    if minute < 24:
        hourServo.angle((hour-1)*15 + 4)
    if minute < 36:
        hourServo.angle((hour-1)*15 + 8)
    if minute < 48:
        hourServo.angle((hour-1)*15 + 11)
    if minute < 60:
        hourServo.angle((hour-1)*15 + 14)

def set_minute_servo(minute):
    print("Doing Something Else")
    minuteServo.angle(minute*3)


hourServo.angle(0)
minuteServo.angle(0)
###########
#code body#
###########

while True:
    timeNOW = time.localtime()
    hour = timeNOW.tm_hour
    minute = timeNOW.tm_min
    set_hour_servo(hour)
    set_minute_servo(minute)




#ENDING I2C Connection!
pca.deinit()