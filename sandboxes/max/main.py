#importing the stuff
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.tools import wait
from pybricks.parameters import Port

hub = PrimeHub()
#defining the motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)
#defining the  left and right turns
def right_turn(degree):
    left_turn (degree * -1)

def left_turn(degree):
    distance_between_wheels = 143
    pi = 3.14159
    wheel_diameter = 88
    wheel_circumfrence = wheel_diameter * pi
    distance_per_turn_degree = distance_between_wheels * pi / 360
    distance_to_rotate = distance_per_turn_degree * degree
    rotation_angle = distance_to_rotate / wheel_circumfrence * 360
    
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_angle(300,  rotation_angle,  wait=False)
    right_motor.run_angle(300, rotation_angle,   wait=False) 
    while not left_motor.done() or not right_motor.done():
        wait(10)

left_turn(90)
wait(10)
right_turn(90)
