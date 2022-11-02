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


def angle(distance):
    return distance/(5.5*math.pi)*360

#torch sensor: 去检测开始的墙（如果我们不考虑用小马达转sound sensor)
def torchSensorMethod():
    left_motor.run(240)
    right_motor.run(240)
    while not (touch_1.pressed() or touch_2.pressed()):
        wait(10)
    left_motor.brake()
    right_motor.brake()
    #reverse by 20cm
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run(-240)
    right_motor.run(-240)
    while left_motor.angle()>=angle(-10) and right_motor.angle()>=angle(-10):
        print(left_motor.angle(),'left')
        print(right_motor.angle(),'right')
    left_motor.brake()
    right_motor.brake()
    
def ultraSoundMethod(): #方法二用ultrasound测距，到达距离让他转90度
    left_motor.run(240)
    right_motor.run(240)
    while ultra.distance() > 300:
        print(ultra.distance())
    left_motor.brake()
    right_motor.brake()
    sound_motor.run_target(90, -55, then=Stop.HOLD, wait=False)
    
def _turnRight(lm, rm):
    gyro.reset_angle(0)
    while gyro.angle() < 80: 
        lm.run(100)
        rm.run(-100)
    lm.run(0)
    lm.run(0)




    
torchSensorMethod()
_turnRight(left_motor, right_motor)
# left_motor.run(240)
# right_motor.run(40)
# wait(1800) #这个时间你看着测试下，转90度，我大概算出来是1800

left_motor.reset_angle(0)
right_motor.reset_angle(0)
left_motor.run(160)
right_motor.run(160)

while True:
    if (left_motor.angle() + right_motor.angle())/2 >= angle(200):
        break
    elif ultra.distance() <=80:
        left_motor.run(180)
        right_motor.run(120)
    else:
        left_motor.run(120)
        right_motor.run(180)
print(ultra.distance())


left_motor.brake()
right_motor.brake()

    