from robot import Robot
from pybricks.parameters import Stop

class Run_02():
    def __init__(self, robot):
        self.robot = robot

    def run(self):
        self.robot.backwards(300,32)
        self.robot.drive_base.turn(50)
        self.robot.drive_base.turn(40)
        self.robot.drive_base.turn(30)
        self.robot.backwards(300,20)
        self.robot.drive_base.turn(12)
        self.robot.drive_base.turn(20)
        self.robot.right_motor.run_time(170, 2200, wait = False)
        self.robot.left_motor.run_time(170, 2200, wait = True)
        self.robot.stop()
        self.robot.attachment_motor.run_angle(1200, 2600)
        self.robot.backwards(300, 48)

    def run2(self):
        self.robot.drive_base.settings(straight_speed = 300, turn_rate = 300)
        self.robot.drive_base.straight(235)
        self.robot.side_motor.run_angle(100, 100)
        self.robot.drive_base.straight(67)
        self.robot.attachment_motor.run_angle(800, 2600)
        self.robot.drive_base.straight(-200)
        self.robot.drive_base.turn(-38)
        self.robot.drive_base.straight(120)
        self.robot.drive_base.turn(8)
        self.robot.drive_base.settings(straight_speed = 300, straight_acceleration = [400, 400], turn_rate = 300)
        self.robot.drive_base.curve(1200, -10, then = Stop.COAST)
        self.robot.drive_base.curve(3100, -20)