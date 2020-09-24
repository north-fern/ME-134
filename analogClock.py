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

###########
#code body#
###########

while True:
    timeNOW = time.localtime()
    hour = timeNOW.tm_hour
    minute = timeNOW.tm_min






#ENDING I2C Connection!
pca.deinit()