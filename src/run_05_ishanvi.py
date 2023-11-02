from mission_base import MissionBase

class Run_05(MissionBase):
    def __init__(self, left_motor, right_motor, attachment_motor, drive_base):
        super().__init__(left_motor, right_motor)
        self.attachment_motor = attachment_motor
        self.drive_base = drive_base

    def run(self):
        self.backwards(300,32)
        self.drive_base.turn(50)
        self.drive_base.turn(40)
        self.drive_base.turn(30)
        self.backwards(300,20)
        self.drive_base.turn(30)
        #self.right_motor.run_time(-180, 2200, wait = False)
        #self.left_motor.run_time(-180, 2200, wait = True)
        self.backwards(300,-19)
        self.attachment_motor.run_angle(1500, 2400)
        self.backwards(300, 48)
