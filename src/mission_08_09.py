from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initilize the hub.
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)
hub = PrimeHub()

def forward(speed,distance):
    cm = 27.6
    left_motor.run_angle(speed, distance/cm * 360, wait=False)
    right_motor.run_angle(speed, distance/cm* -360, wait=False)
    while not left_motor.done() or not right_motor.done():
        wait(10)

def backwards(speed,distance):
    forward(speed,-distance)

def right_turn(degree):
    left_turn((-1)*degree)

def left_turn(degree):
    distance_between_wheels = 143
    pi = 3.14159
    wheel_diameter = 88
    # calculating the wheel circumfrence - wheel diameter multiplied by pi
    wheel_circumfrence = wheel_diameter * pi
    # calculating the distance the wheel needs to spin
    distance_to_rotate = distance_between_wheels * pi / 360 * degree 
    # calculating how many times the wheel needs to turn, and then converts it to degrees
    rotation_angle = distance_to_rotate / wheel_circumfrence * 360
    #reset_angle after every movementt makes the robot's movements more accurate
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

    # wait = false makes it so that both motors start running at the same time
    # if wait = true then the program would wait for one motor to finish turning
    speed = 100

    left_motor.run_angle(speed, rotation_angle, wait=False)
    right_motor.run_angle(speed, rotation_angle, wait=False) 
    while not left_motor.done() or not right_motor.done():
        wait(10)

forward(200,45)
backwards(1000, 45)
