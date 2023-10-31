from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from mission_base import MissionBase

class Run_01(MissionBase):
    def __init__(self, drive_base, left_motor, right_motor):
        super().__init__(left_motor, right_motor)
        self.drive_base = drive_base
    
    def nudge_lever(self):
        distance = 250
        self.drive_base.straight(distance)
        self.drive_base.turn(-20)
        self.drive_base.turn(20)
        self.drive_base.straight(-distance)

    def mission_02(self):
        self.forward(500,65)
        self.drive_base.turn(-40)
        self.backwards(100,5)
        self.forward(800,15)
        self.backwards(100,13)
        self.forward(800, 20)
        self.backwards(200,8)
        self.drive_base.turn(40)
        self.backwards(1000,63)
    
    def push_camera(self):
       self.forward(200,45)
       self.backwards(1000, 45)