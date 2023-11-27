from pybricks.tools import wait
from mission_base import MissionBase

class Run_02(MissionBase):
    def __init__(self, robot):
        self.robot = robot

    def weird_10(self):
        self.robot.drive_base.straight(370)
        self.robot.drive_base.straight(-35)
        self.robot.attachment_motor.turn_angle(30000, -170)
        self.robot.turn(50)
        wait(500)
        self.robot.drive_base.straight(-37)
        self.robot.attachment_motor.turn_angle(30000, 170)