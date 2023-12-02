from pybricks.tools import wait
from robot import Robot

class Run_01():
    def __init__(self, robot):
        self.robot = robot

    def run(self):
        # (straight_speed, straight_acceleration, turn_rate, turn_acceleration)
        self.robot.drive_base.settings(straight_speed = 250)
        self.robot.drive_base.curve(500, -92)
        self.robot.drive_base_settings = self.robot.drive_base.settings()
        self.robot.drive_base.settings(turn_rate = 60)
        self.robot.drive_base.turn(59)
        self.robot.drive_base.straight(30)
        # drop off masterpiece
        self.robot.drive_base.straight(-70)
        self.robot.drive_base.turn(67)
        self.robot.drive_base.straight(70)
        self.robot.drive_base.straight(-25)
        self.robot.drive_base.settings(straight_speed = 500, turn_rate = 200)
        # nodge augmented reality statue
        self.robot.drive_base.turn(61)
        self.robot.drive_base.straight(370)
        self.robot.drive_base.turn(100)
        # push hologram performer
        self.robot.drive_base.straight(-70)
        self.robot.drive_base.settings(straight_speed = 900, straight_acceleration = [500, 500])
        # curve back to home
        self.robot.drive_base.curve(860, -30)



