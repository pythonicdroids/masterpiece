from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from mission_base import MissionBase

class Run_01():
    def __init__(self, robot):
        self.robot = robot
    
    def nudge_lever(self):
        distance = 250
        self.robot.drive_base.straight(distance)
        self.robot.drive_base.turn(-20)
        self.robot.drive_base.turn(20)
        self.robot.drive_base.straight(-distance)

    def mission_02(self):
        self.robot.backwards(500,65)
        self.robot.drive_base.turn(-40)
        self.robot.forward(100,5)
        self.robot.backwards(800,15)
        self.robot.forward(100,13)
        self.robot.backwards(800, 20)
        self.robot.forward(200,8)
        self.robot.drive_base.turn(40)
        self.robot.forward(1000,63)
    
    def push_camera(self):
       self.robot.backwards(200,45)
       self.robot.forward(1000, 45)

    def mission_8_and_9(self):
       #self.robot.drive_base.straight(200)
       self.robot.drive_base.straight(200)
       self.robot.attachment_motor.run_angle(200, 400)
       wait(1000)
       self.robot.drive_base.straight(-290)
       self.robot.attachment_motor.run_angle(700, -380)
