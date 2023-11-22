class Run_06:
    def __init__(self, robot):
        self.robot = robot

    def run(self):
        self.robot.drive_base.straight(200)
        self.robot.drive_base.turn(-20)
        self.robot.drive_base.straight(220)
        self.robot.drive_base.turn(60)
        self.robot.drive_base.straight(130)
               
        self.robot.drive_base.straight(-100)
        self.robot.drive_base.turn(90)
        self.robot.drive_base.straight(300)
