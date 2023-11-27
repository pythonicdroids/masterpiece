from mission_base import MissionBase

class Run_00(MissionBase):
    def __init__(self, left_motor, right_motor, side_motor, attachment_motor, drive_base):
        super().__init__(left_motor, right_motor, side_motor)
        self.attachment_motor = attachment_motor
        self.drive_base = drive_base
        

    def run(self):
        light_show_turn_angle = 475
        
        
        self.drive_base.straight(940) 
        self.drive_base.turn(-85) 
        self.drive_base.straight(10)
        self.drive_base.turn(-5)
        self.drive_base.straight(105) 
        self.attachment_motor.run_angle(1000, 300)
        self.attachment_motor.run_angle(1000, -40) 
        self.attachment_motor.run_angle(250, light_show_turn_angle - 260)
        self.attachment_motor.run_time(-1000, 500)
        self.drive_base.straight(-115)
        #self.side_motor.run_angle(100, -97, wait = False)
        self.drive_base.turn(-45)
        self.drive_base.straight(260)
        #self.side_motor.run_angle(500,30)
        self.side_motor.run_time(150,400)
        self.drive_base.turn(-60)
        self.drive_base.straight(700)
        self.side_motor.run_angle(1000,-30)
      


