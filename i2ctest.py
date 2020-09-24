import smbus
bus = smbus.SMBus(1)
import time
'''
A basis (and examples) for the SMBus commands and information on the registers to use
 (and generally how to use) for the IMU come from here

https://www.programcreek.com/python/?project_name=MarkSherstan%2FMPU-6050-9250-I2C-CompFilter

Other information comes from the askPython website (on how to use strings, absolute values, convert floats to strings)

Help on setting up the i2c lines (physically) came from Jeremy, who helped me debug my wires. Turns out I soldered my pins
upside down and the ribbon cable doesn't work as it says on the breakout board. Help setting up remote SSH from home also
came from Jeremy, who provided insight into the error I was getting, and helped me figure out how to clear my fingerprints
'''

DEV_ADDRESS = 0x68
DEC_REG_MO = 0x6B

acelx = 0
acely = 0
acelz = 0
counter = 0
val = bus.write_byte_data(DEV_ADDRESS, DEC_REG_MO, 0x00)

print("Calibrating IMU. Please leave on a flat surface!")
time.sleep(2)
for x in range(40):
        acelx = acelx + (bus.read_byte_data(DEV_ADDRESS, 0x43))
        acely = acely + (255-bus.read_byte_data(DEV_ADDRESS,0x45))
        acelz = acelz + (255-bus.read_byte_data(DEV_ADDRESS, 0x047))
        counter = counter + 1

acelxx = acelx / counter
acelyy = acely / counter
acelzz = acelz / counter
#print(type(acelxx))
#print(type(acelyy))
#print(type(acelzz))
print("Calibration values are X: " + str(acelxx) +  " Y: " +str(acelyy)+ " Z: "+str( acelzz))

time.sleep(5)
print("Begin Moving IMU")
time.sleep(1)

while True:
        xacel = acelxx - (bus.read_byte_data(DEV_ADDRESS, 0x43))
        yaccel = acelyy - (bus.read_byte_data(DEV_ADDRESS, 0x45))
        zaccel = acelzz - (bus.read_byte_data(DEV_ADDRESS, 0x47))
        print("X: " + str(abs(xacel)) + " Y: " + str(abs(yaccel)) + " Z: " + str(abs(zaccel)))
