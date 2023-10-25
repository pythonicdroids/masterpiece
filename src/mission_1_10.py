from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
hub = PrimeHub()
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)
front_motor = Motor(Port.D)
def left_turn(speed,degree):
    distance_between_wheels = 143
    pi = 3.14159
    wheel_diameter = 88
    wheel_circumfrence = wheel_diameter * pi
    distance_per_turn_degree = distance_between_wheels * pi / 360
    wait(10)
    distance_to_rotate = distance_per_turn_degree * degree
    rotation_angle = distance_to_rotate / wheel_circumfrence * 360
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_angle(speed,  rotation_angle,  wait=False)
    right_motor.run_angle(speed, rotation_angle,   wait=False) 
    while not left_motor.done() or not right_motor.done():
        wait(10)
def right_turn(speed,degree):
    left_turn(speed,degree * -1)
def forward(speed,distance):
   c_cm = 27.6
   left_motor.run_angle(speed, -distance/c_cm * 360, wait=False)
   right_motor.run_angle(speed, distance/c_cm * 360, wait=False)
   while not left_motor.done() or not right_motor.done():
      wait(10)
def frontmotor(speed,degree):
    distance_between_wheels = 143
    pi = 3.14159
    wheel_diameter = 88
    wheel_circumfrence = wheel_diameter * pi
    distance_per_turn_degree = distance_between_wheels * pi / 360
    wait(10)
    distance_to_rotate = distance_per_turn_degree * degree
    rotation_angle = distance_to_rotate / wheel_circumfrence * 360
    front_motor.reset_angle(0)
    front_motor.run_angle(speed,  rotation_angle,  wait= True) 
def mission_one_ten():
    left_turn(450,27)
    frontmotor(1000,400)
    forward(200,31)
    right_turn(200,115)
    forward(200,40)
    frontmotor(1000,-400)
    left_turn(200,49)
    forward(200,6)
    frontmotor(750,1400)
    frontmotor(750,-1400)
    left_turn(200, 10)
    forward(200,0.3)
    frontmotor(750,1400)
    forward(200,-5)
def mission_one():
    left_turn(450,28.25)
    frontmotor(1000,300)
    forward(200,30.5)
    right_turn(200,200)
def mission_ten():
    forward(200,44)
    frontmotor(750,1400)
    frontmotor(750,-1400)
    left_turn(200, 10)
    forward(200,0.3)
    frontmotor(750,1400)
    forward(200,-5)
mission_one()
