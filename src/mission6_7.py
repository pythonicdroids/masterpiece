
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

c_cm = 27.6
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
attachment_motor = Motor(Port.D)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter = 56, axle_track = 112)

#rive_base.straight(200)
def attachment(speed, distance):
    attachment_motor.run_angle(speed, -distance/c_cm * 360)
drive_base.straight(200)
drive_base.turn(-20)
drive_base.straight(200)
drive_base.turn(50)
drive_base.straight(150)
attachment(1500,10)
drive_base.straight(-100)
drive_base.turn(90)
drive_base.straight(300)