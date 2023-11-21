class Run_06:
    def __init__(self, drive_base, attachment_motor, side_motor):
        self.drive_base = drive_base
        self.attachment_motor = attachment_motor
        self.side_motor = side_motor

    def run(self):
        self.drive_base.straight(200)
        self.drive_base.turn(-20)
        self.drive_base.straight(220)
        self.drive_base.turn(60)
        self.drive_base.straight(130)
               
        self.drive_base.straight(-100)
        self.drive_base.turn(90)
        self.drive_base.straight(300)
