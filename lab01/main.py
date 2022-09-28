#!/usr/bin/env pybricks-micropython

# Yumo Bai PID: 730480742
# Peiyu Li PID: 730434819

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
import math

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Initialize the motors and sensors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
ultra = UltrasonicSensor(Port.S1)
touch_1 = TouchSensor(Port.S2)
touch_2 = TouchSensor(Port.S3)
gyro = GyroSensor(Port.S4)
stopWatch = StopWatch()

left_motor.run(240)
right_motor.run(240)

def angle(distance):
    return distance/(5.5*math.pi)*360

def correction():
    if(left_motor.angle()<right_motor.angle()):
        left_motor.run_angle(5, right_motor.angle()-left_motor.angle(), then=Stop.HOLD, wait=True)
    if(left_motor.angle()>right_motor.angle()):
        right_motor.run_angle(5, abs(right_motor.angle()-left_motor.angle()), then=Stop.HOLD, wait=True)
    right_motor.brake()
    left_motor.brake()
    


while left_motor.angle()<=angle(120) and right_motor.angle()<=angle(120):
     print(left_motor.angle(),'left')
     print(right_motor.angle(),'right')
left_motor.brake()
right_motor.brake()
correction()
ev3.speaker.beep()

pressed = Button.CENTER in ev3.buttons.pressed()
while not pressed:
    pressed = Button.CENTER in ev3.buttons.pressed()
    
#move to 50cm mark:
left_motor.run(240)
right_motor.run(240)
while(ultra.distance()>=505):
    print(ultra.distance())
wait(10)
while(ultra.distance()>=503):
    print('distance checked')
left_motor.brake()
right_motor.brake()
ev3.speaker.beep()

pressed = Button.CENTER in ev3.buttons.pressed()
while not pressed:
    pressed = Button.CENTER in ev3.buttons.pressed()
    
#torch sensor:
left_motor.run(240)
right_motor.run(240)
while not (touch_1.pressed() or touch_2.pressed()):
    wait(10)

left_motor.brake()
right_motor.brake()
ev3.speaker.beep()


pressed = Button.CENTER in ev3.buttons.pressed()
while not pressed: 
    pressed = Button.CENTER in ev3.buttons.pressed()
    
#reverse by 50cm
left_motor.reset_angle(0)
right_motor.reset_angle(0)
left_motor.run(-240)
right_motor.run(-240)

while left_motor.angle()>=angle(-50) and right_motor.angle()>=angle(-50):
    print(left_motor.angle(),'left')
    print(right_motor.angle(),'right')
left_motor.brake()
right_motor.brake()

# Write your program here.
ev3.speaker.beep()
