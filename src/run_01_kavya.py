from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from mission_base import MissionBase

class Run_01(MissionBase):
    def __init__(self, drive_base, left_motor, right_motor, side_motor, attachment_motor):
        super().__init__(left_motor, right_motor, side_motor)
        self.attachment_motor = attachment_motor
        self.drive_base = drive_base
    
    def nudge_lever(self):
        distance = 250
        self.drive_base.straight(distance)
        self.drive_base.turn(-20)
        self.drive_base.turn(20)
        self.drive_base.straight(-distance)

    def mission_02(self):
        self.backwards(500,65)
        self.drive_base.turn(-40)
        self.forward(100,5)
        self.backwards(800,15)
        self.forward(100,13)
        self.backwards(800, 20)
        self.forward(200,8)
        self.drive_base.turn(40)
        self.forward(1000,63)
    
    def push_camera(self):
       self.backwards(200,45)
       self.forward(1000, 45)

    def mission_01(self):
        turn_angle = 450
        self.drive_base.straight(185)
        self.attachment_motor.run_angle(100, turn_angle)
        self.drive_base.straight(-160)
        wait(1000)
        self.drive_base.straight(-80)
        self.attachment_motor.run_angle(100, -turn_angle)
        self.drive_base.straight(-150)