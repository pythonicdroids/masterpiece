class Run_06:
    def __init__(self, drive_base, attachment_motor):
        self.drive_base = drive_base
        self.attachment_motor = attachment_motor

    def run(self):
        c_cm = 27.6
        speaker_turn_angle = 100

        self.drive_base.straight(200)
        self.drive_base.turn(-20)
        self.drive_base.straight(190)
        self.drive_base.turn(60)
        self.drive_base.straight(120)
        
        # retry once to make sure the speakers are indeed turned
        self.attachment_motor.run_angle(5000, speaker_turn_angle/c_cm * 360)
        #self.attachment_motor.run_angle(1500, -speaker_turn_angle/c_cm * 360)
        #self.attachment_motor.run_angle(5000, speaker_turn_angle/c_cm * 360)
        
        self.drive_base.straight(-100)
        self.drive_base.turn(90)
        self.drive_base.straight(300)