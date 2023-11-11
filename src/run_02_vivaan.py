from pybricks.tools import wait
from mission_base import MissionBase

class Run_02(MissionBase):
    def __init__(self, left_motor, right_motor, side_motor, front_motor):
        super().__init__(left_motor, right_motor, side_motor)
        self.front_motor = front_motor

    def frontmotor(self,speed,degree):
        distance_between_wheels = 143
        pi = 3.14159
        wheel_diameter = 88
        wheel_circumfrence = wheel_diameter * pi
        distance_per_turn_degree = distance_between_wheels * pi / 360
        wait(10)
        distance_to_rotate = distance_per_turn_degree * degree
        rotation_angle = distance_to_rotate / wheel_circumfrence * 360
        self.front_motor.reset_angle(0)
        self.front_motor.run_angle(speed,  rotation_angle,  wait= True) 

    def mission_one_ten(self):
        #self.left_turn(450,27)
        self.frontmotor(1000,400)
        #self.forward(200,31)
        #self.right_turn(200,115)
        self.forward(500,50)
        self.left_turn(500,45)
        self.forward(500,20)
        self.right_turn(500,45)
        self.forward(200,40)
        self.frontmotor(1000,-400)
        self.left_turn(200,49)
        self.forward(200,6)
        self.frontmotor(750,1400)
        self.frontmotor(750,-1400)
        self.left_turn(200, 10)
        self.forward(200,0.3)
        self.frontmotor(750,1400)
        self.forward(200,-5)
    def mission_one(self):
        self.left_turn(20, 450)
        self.forward(500,22)
        self.right_motor.run_time(-200, 600, wait = False)
        self.left_motor.run_time(200, 600, wait = True)
        self.forward(500,-25)
    def mission_ten(self):
        self.forward(200,44)
        self.frontmotor(750,1400)
        self.frontmotor(750,-1400)
        self.left_turn(200, 10)
        self.forward(200,0.3)
        self.frontmotor(750,1400)
        self.forward(200,-5)
    def reset_frontmotor(self):
        self.frontmotor(500,-400)