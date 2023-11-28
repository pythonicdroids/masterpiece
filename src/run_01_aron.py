from pybricks.tools import wait
from robot import Robot

class Run_01():
    def __init__(self, robot):
        self.robot = robot

    def run(self):
        self.robot.drive_base.curve(500, -92)
        self.robot.drive_base_settings = self.robot.drive_base.settings()
        self.robot.drive_base.settings(turn_rate = 50)
        self.robot.drive_base.turn(59)
        self.robot.drive_base.straight(30)
        self.robot.drive_base.straight(-70)
        self.robot.drive_base.turn(67)
        self.robot.drive_base.straight(100)
        self.robot.drive_base.straight(-10)
        self.robot.drive_base.settings(straight_speed = 200, turn_rate = 100)
        self.robot.drive_base.turn(62)
        self.robot.drive_base.straight(380)
        self.robot.drive_base.turn(90)
        self.robot.drive_base.straight(-70)
        self.robot.drive_base.curve(1000, -30)



