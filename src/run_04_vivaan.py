from pybricks.tools import wait

class Run_04():
    def __init__(self, robot):
        self.robot = robot

    def frontmotor(self,speed,degree):
        distance_between_wheels = 143
        pi = 3.14159
        wheel_diameter = 88
        wheel_circumfrence = wheel_diameter * pi
        distance_per_turn_degree = distance_between_wheels * pi / 360
        wait(10)
        distance_to_rotate = distance_per_turn_degree * degree
        rotation_angle = distance_to_rotate / wheel_circumfrence * 360
        self.robot.attachment_motor.reset_angle(0)
        self.robot.attachment_motor.run_angle(speed,  rotation_angle,  wait=True) 

    def mission_ten(self):
        self.robot.drive_base.straight(230)
        self.robot.drive_base.straight(-20)
        self.frontmotor(1800,1500)
        self.robot.drive_base.turn(5)
        self.robot.drive_base.turn(5)
        self.robot.drive_base.turn(10)
        wait(1000)
        self.robot.drive_base.turn(150)
        self.robot.drive_base.straight(25)
        self.frontmotor(1800,-1500)

    def mission_10(self):
        self.robot.drive_base.straight(250)
        self.robot.drive_base.straight(-15)
        self.robot.attachment_motor.run_angle(3000, -340)
        self.robot.drive_base.turn(5)
        wait(500)
        self.robot.drive_base.straight(-37)
        self.robot.attachment_motor.run_angle(30000, 340)