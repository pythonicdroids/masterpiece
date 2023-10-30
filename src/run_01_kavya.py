from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

class Run_01:
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
    
    def forward(self, speed,distance):
        cm = 27.6
        self.left_motor.run_angle(speed, distance/cm * 360, wait=False)
        self.right_motor.run_angle(speed, distance/cm* -360, wait=False)
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)
    
    def backwards(self, speed,distance):
        self.forward(speed,-distance)
    
    def right_turn(self, degree):
        self.left_turn((-1)*degree)
    
    def left_turn(self, degree):
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
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
    
        # wait = false makes it so that both motors start running at the same time
        # if wait = true then the program would wait for one motor to finish turning
        speed = 100
    
        self.left_motor.run_angle(speed, rotation_angle, wait=False)
        self.right_motor.run_angle(speed, rotation_angle, wait=False) 
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)

    def nudge_lever(self):
        self.backwards(speed=300, distance=40)
        self.left_turn(25)
        self.right_turn(10)
        self.forward(1000,45)

    def mission_02(self):
        self.forward(500,63)
        self.left_turn(50)
        self.backwards(100,5)
        self.forward(800,15)
        self.backwards(100,13)
        self.forward(800, 20)
        self.backwards(200,8)
        self.right_turn(60)
        self.backwards(1000,63)
    
    def push_camera(self):
       self.forward(200,45)
       self.backwards(1000, 45)