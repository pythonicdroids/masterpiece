from mission_base import MissionBase

class Run_05(MissionBase):
    def __init__(self, left_motor, right_motor, attachment_motor, drive_base):
        super().__init__(left_motor, right_motor)
        self.attachment_motor = attachment_motor
        self.drive_base = drive_base

    def run(self):
        self.backwards(300,32)
        self.drive_base.turn(50)
        self.drive_base.turn(70)
        self.backwards(300,20)
        self.drive_base.turn(35)
        self.backwards(300,-22)
        self.attachment_motor.run_angle(1500, 2300)
        self.backwards(300, 48)
