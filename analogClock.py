'''
For reference in learing how to control the servos with the adafruit 
motor and adafruit pca libraries, the following website was helpful in
showing examples on how to use the code properly

https://github.com/adafruit/Adafruit_CircuitPython_PCA9685/blob/master/
examples/pca9685_servo.py

'''
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

'''
This function takes the minutes and hours value from the date-time and sets the hour
hand to the proper angle based on how far along the hour it is i.e. if the time is closer to
6 than 5, aka 5:45, the hour indicator will be closer to the 6 notation that the 5 notation
'''
def set_hour_servo(hour, minute):
    print("Doing Something HOURS")
    if hour > 12:
        hourNEW = hour%12
        hour = hourNEW
        print(hour)

    if hour == 0:
        hour = 12

    if minute < 12:
        angle = ((hour-1)*15 + 0)
        hourServo.angle = (angle)
        print(angle)
    elif minute < 24:
        angle = ((hour-1)*15 + 3)
        hourServo.angle = (angle)
        print(angle)
    elif minute < 36:
        angle = ((hour-1)*15 + 6)
        hourServo.angle = (angle)
        print(angle)
    elif minute < 48:
        angle = ((hour-1)*15 + 9)
        hourServo.angle = (angle)
        print(angle)
    elif minute < 60:
        angle = ((hour-1)*15 + 12)
        hourServo.angle = (angle)
        print(angle)

'''
This function takes the minutes value from the date-time and sets the angle of the 
minute-controling servo to 3* the minute number
'''
def set_minute_servo(minute):
    print("Doing Something Else MINUTES")
    angle = minute*3
    minuteServo.angle = (angle)
    print(angle)

''' 
This function takes the time on the clock and runs it as normal
'''
def normal_time():
    while True:
        timeNOW = time.localtime()
        hour = timeNOW.tm_hour
        minute = timeNOW.tm_min
        print("The time is: " + str(hour) + ":" + str(minute))
        set_hour_servo(hour, minute)
        set_minute_servo(minute)
 
        time.sleep(10)


'''
This function progresses at 4 times the normal rate of a clock 
to demonstrate the functionality of the clock
'''
def rapid_time():
    hour = 0
    minute = 0
    while True:
            set_hour_servo(hour, minute)
            set_minute_servo(minute)
            time.sleep(.25)
            minute = minute + 1
            if minute == 60:
                hour = hour + 1
                minute = 0
            if hour == 13:
                hour = 1


'''
This function should demonstrate the clock moving to a specific time

'''

def preset():
    preset_hour = int(input("WHAT HOUR? "))
    preset_min = int(input("WHAT MINUTES? "))

    set_hour_servo(preset_hour, preset_min)
    set_minute_servo(preset_min)

###########
#code body#
###########
hourServo.angle = (0)
minuteServo.angle = (0)

button = input("Button Input: Type R for Rapid, N for normal, P for Pre-Set")
if button == 'N':
    normal_time()
elif button == 'R':
    rapid_time()
elif button == "P":
    preset()

#ENDING I2C Connection!
pca.deinit()
