class Mission_06_07:
    def __init__(self, drive_base, attachment_motor):
        self.drive_base = drive_base
        self.attachment_motor = attachment_motor

    def run(self):
        c_cm = 27.6
        speaker_turn_angle = -10

        self.drive_base.straight(200)
        self.drive_base.turn(-20)
        self.drive_base.straight(200)
        self.drive_base.turn(50)
        self.drive_base.straight(150)
        
        # retry once to make sure the speakers are indeed turned
        self.attachment_motor.run_angle(1500, speaker_turn_angle/c_cm * 360)
        self.attachment_motor.run_angle(1500, -speaker_turn_angle/c_cm * 360)
        self.attachment_motor.run_angle(1500, speaker_turn_angle/c_cm * 360)
        
        self.drive_base.straight(-100)
        self.drive_base.turn(90)
        self.drive_base.straight(300)

        self.attachment_motor.run_angle(1500, -speaker_turn_angle/c_cm * 360)
