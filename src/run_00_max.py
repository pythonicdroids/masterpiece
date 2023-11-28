class Run_00():
    def __init__(self, robot):
        self.robot = robot
        

    def run(self):
        light_show_turn_angle = 475
     
        self.robot.drive_base.straight(940) 
        self.robot.drive_base.turn(-85) 
        self.robot.drive_base.straight(10)
        self.robot.drive_base.turn(-5)
        self.robot.drive_base.straight(105) 
        self.robot.attachment_motor.run_angle(1000, 300)
        self.robot.attachment_motor.run_angle(1000, -40) 
        self.robot.attachment_motor.run_angle(250, light_show_turn_angle - 260)
        self.robot.attachment_motor.run_time(-1000, 500)
        self.robot.drive_base.straight(-115)
        #self.robot.side_motor.run_angle(100, -97, wait = False)
        self.robot.drive_base.turn(-45)
        self.robot.drive_base.straight(260)
        #self.robot.side_motor.run_angle(500,30)
        self.robot.side_motor.run_time(150,400)
        self.robot.drive_base.turn(-60)
        self.robot.drive_base.straight(700)
        self.robot.side_motor.run_angle(1000,-30)
      


