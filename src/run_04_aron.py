from pybricks.tools import wait
from mission_base import MissionBase

class Run_04(MissionBase):
    def __init__(self, left_motor, right_motor, side_motor, drive_base):
        super().__init__(left_motor, right_motor, side_motor)
        self.drive_base = drive_base


    def run(self):
        # settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
        self.drive_base.curve(500, -92)
        self.drive_base_settings = self.drive_base.settings()
        self.drive_base.settings(turn_rate = 50)
        self.drive_base.turn(59)
        self.drive_base.straight(30)
        self.drive_base.straight(-70)
        self.drive_base.turn(70)
        self.drive_base.straight(100)
        self.drive_base.settings(straight_speed = 200, turn_rate = 100)
        self.drive_base.turn(62)
        self.drive_base.straight(380)
        self.drive_base.turn(90)
        self.drive_base.straight(-70)
        self.drive_base.curve(1000, -30)



