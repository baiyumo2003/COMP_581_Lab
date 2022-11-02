#!/usr/bin/env pybricks-micropython

# Yumo Bai PID: 730480742
# Peiyu Li PID: 730434819

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Button, Stop, Direction
from pybricks.tools import wait, StopWatch
import math

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors and sensors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
ultra = UltrasonicSensor(Port.S1)
touch_1 = TouchSensor(Port.S2)
touch_2 = TouchSensor(Port.S3)
gyro = GyroSensor(Port.S4)
gyro.reset_angle(0)
stopWatch = StopWatch()

speed = 250
d = 56
c = d * math.pi
time = 2100 / c * 360 / speed * 1000
reduced_time = 203.2 / c * 360 / speed * 1000
base_dis = 0

def angle(distance):
    return distance/(5.5*math.pi)*360

def tune(lm, rm):
    while not touch_1.pressed() or not touch_2.pressed():
        lm.run(250)
        rm.run(250)
    lm.run(-100) 
    rm.run(-100)
    wait(1100)
    _turnRight(lm, rm)

def _turnRight(lm, rm):
    gyro.reset_angle(0)
    while gyro.angle() < 80: 
        lm.run(100)
        rm.run(-100)
    lm.run(0)
    lm.run(0)

leftDis=0
rightDis=0
tune(left_motor, right_motor)
base_dis = ultra.distance()
stopWatch.reset()
left_motor.reset_angle(0)
right_motor.reset_angle(0)
while stopWatch.time() < time and (left_motor.angle()+right_motor.angle)/2<angle(200):
    stopWatch.resume()
    left_motor.run(250)
    right_motor.run(250)
    leftDis=left_motor.angle()
    rightDis=right_motor.angle()

    # wall bend inward
    if touch_1.pressed():
        stopWatch.pause()
        while not touch_2.pressed():    
            left_motor.run(0)
            right_motor.run(250)
            left_motor.reset_angle(leftDis)
            right_motor.reset_angle(rightDis)
        tune(left_motor, right_motor)
        left_motor.reset_angle(leftDis)
        right_motor.reset_angle(rightDis)
        # time -= reduced_time
        base_dis = ultra.distance()

    stopWatch.resume()

    # wall bend outward
    if ultra.distance() > base_dis + 500:
        stopWatch.pause()
        left_motor.run(100)
        right_motor.run(100) 
        wait(1500)
        while gyro.angle() > 3:
            left_motor.run(-100)
            right_motor.run(100)
            left_motor.reset_angle(leftDis)
            right_motor.reset_angle(rightDis)
        tune(left_motor, right_motor)
        # time -= reduced_time
        left_motor.reset_angle(leftDis)
        right_motor.reset_angle(rightDis)
        base_dis = ultra.distance()
    stopWatch.resume()

ev3.speaker.beep()