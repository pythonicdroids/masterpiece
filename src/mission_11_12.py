from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

left_motor = Motor(Port.A)
right_motor = Motor(Port.E)
wheel_distance = 128
rotation_per_distance = 276
rotation_per_turn = wheel_distance * 3.14159 / 360
front_attachment_motor = Motor(Port.D)

def forward(speed, distance_cm):
    circ_cm = 27.6
    left_motor.run_angle(speed, -distance_cm/circ_cm * 360, wait = False)
    right_motor.run_angle(speed, distance_cm/circ_cm * 360, wait = False)
    while not left_motor.done() or not right_motor.done():
        wait(10)

def backwards(speed, distance_cm):
    forward(speed, -distance_cm)

forward(300, 48)
front_attachment_motor.run_angle(1500, 2300)
backwards(300, 50)
