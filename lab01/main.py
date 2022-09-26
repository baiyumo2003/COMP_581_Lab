#!/usr/bin/env pybricks-micropython
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
stopWatch = StopWatch()


speed = 360
d = 56
c = d * math.pi
time = 1200 / c * 360 / speed * 1000

task = [True, False, False]
gyro.reset_angle(0)
print(gyro.angle())
while True:
    if Button.CENTER in ev3.buttons.pressed() and task[0] == True:
        stopWatch.reset()
        
        while stopWatch.time() < time:
            # print(stopWatch.time())
            print(gyro.angle())
            ori_diff = gyro.angle()
            if ori_diff >= -3 and ori_diff <= 3:
                stopWatch.resume()
                left_motor.run(360) 
                right_motor.run(360)
            elif ori_diff < -3:
                stopWatch.pause()
                # print(stopWatch.time())
                while gyro.angle() < -2: 
                    left_motor.run(10) 
                    right_motor.run(-10)
            else:
                stopWatch.pause()
                # print(stopWatch.time())
                while gyro.angle() > 4:
                    left_motor.run(-10)
                    right_motor.run(10)
        if gyro.angle() < -3:
            while gyro.angle() < -2: 
                left_motor.run(10) 
                right_motor.run(-10)
        if gyro.angle() > 3:
            while gyro.angle() > 4:
                left_motor.run(-10)
                right_motor.run(10)
                
        left_motor.brake()
        right_motor.brake()
        ev3.speaker.beep()
        task[0] = False
    #     task[1] = True
    # if Button.CENTER in ev3.buttons.pressed() and task[1] == True:
    #     print("doing task 2")
    #     while ultra.distance() > 501:
    #         left_motor.run(100)
    #         right_motor.run(100)
    #     left_motor.brake()
    #     right_motor.brake()
    #     print(ultra.distance())
    #     wait(10)
    #     ev3.speaker.beep()
    #     task[1] = False
    #     task[2] = True
    # if Button.CENTER in ev3.buttons.pressed() and task[2] == True:
    #     print("doing task 3")
    #     while not touch_1.pressed() or not touch_2.pressed():
    #         left_motor.run(360)
    #         right_motor.run(360)
    #     left_motor.run(0)
    #     right_motor.run(0)
    #     wait(10)
    #     while ultra.distance() <= 499:
    #         left_motor.run(-100)
    #         right_motor.run(-100)
    #     left_motor.run(0)
    #     right_motor.run(0)
    #     print(ultra.distance())
    #     task[2] = False
    # if not task[0] and not task[1] and not task[2]:
    #     break