from pybricks.tools import wait

class Mission_01_10:
    def __init__(self, left_motor, right_motor, front_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.front_motor = front_motor
    
    def left_turn(self, speed, degree):
        distance_between_wheels = 143
        pi = 3.14159
        wheel_diameter = 88
        wheel_circumfrence = wheel_diameter * pi
        distance_per_turn_degree = distance_between_wheels * pi / 360
        wait(10)
        distance_to_rotate = distance_per_turn_degree * degree
        rotation_angle = distance_to_rotate / wheel_circumfrence * 360
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        self.left_motor.run_angle(speed,  rotation_angle,  wait=False)
        self.right_motor.run_angle(speed, rotation_angle,   wait=False) 
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)
    def right_turn(self, speed, degree):
        self.left_turn(speed,degree * -1)
    
    def forward(self, speed, distance):
        c_cm = 27.6
        self.left_motor.run_angle(speed, -distance/c_cm * 360, wait=False)
        self.right_motor.run_angle(speed, distance/c_cm * 360, wait=False)
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)
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
        self.left_turn(450,27)
        self.frontmotor(1000,400)
        self.forward(200,31)
        self.right_turn(200,115)
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
        self.left_turn(450,28.25)
        self.frontmotor(1000,300)
        self.forward(200,30.5)
        self.right_turn(200,200)
    def mission_ten(self):
        self.forward(200,44)
        self.frontmotor(750,1400)
        self.frontmotor(750,-1400)
        self.left_turn(200, 10)
        self.forward(200,0.3)
        self.frontmotor(750,1400)
        self.forward(200,-5)
    