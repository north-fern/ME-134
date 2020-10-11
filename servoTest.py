import time
from adafruit_motor import servo
from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685

i2c_bus  = busio.I2C(SCL, SDA)

pca = PCA9685(i2c_bus)

pca.frequency = 50

servo0 = servo.Servo(pca.channels[0])
#servo1 = servo.Servo(pca.channels[6])
print("STARTING TEST")

for i in range(180):
        servo0.angle = i
       # servo1.angle = i
        time.sleep(.1)
stop = input("CONTINUE TEST? ")

print("ENDING TEST")

for i in range(180):
        servo0.angle = 180-i
        #servo1.angle = 180 - i
        time.sleep(.1)

print("TEST COMPLETE")
pca.deinit()