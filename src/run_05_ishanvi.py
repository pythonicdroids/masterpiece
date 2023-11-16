from mission_base import MissionBase

class Run_05(MissionBase):
    def __init__(self, left_motor, right_motor, side_motor, attachment_motor, drive_base):
        super().__init__(left_motor, right_motor, side_motor)
        self.attachment_motor = attachment_motor
        self.drive_base = drive_base

    def run(self):
        self.backwards(300,32)
        self.drive_base.turn(50)
        self.drive_base.turn(40)
        self.drive_base.turn(30)
        self.backwards(300,20)
        self.drive_base.turn(12)
        self.drive_base.turn(20)
        self.right_motor.run_time(170, 2200, wait = False)
        self.left_motor.run_time(170, 2200, wait = True)
        self.stop()
        #self.backwards(250,-19)
        self.attachment_motor.run_angle(1200, 2600)
        self.backwards(300, 48)

    def run2(self):
        self.drive_base.straight(235)
        self.side_motor.run_angle(100, 100)
        self.drive_base.straight(67)
        self.attachment_motor.run_angle(800, 2600)
        self.drive_base.straight(-200)
        self.drive_base.turn(-38)
        self.drive_base.straight(120)
        self.drive_base.turn(8)
        self.drive_base.curve(1200, -10)
        self.drive_base.straight(500)
        self.drive_base.turn(-40)
        self.drive_base.straight(200)