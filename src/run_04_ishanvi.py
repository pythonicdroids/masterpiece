from motor_utils import MotorUtils
from pybricks.robotics import DriveBase
class Run_04:
    def __init__(self, left_motor, right_motor, attachment_motor, drive_base):
        self.motor_utils = MotorUtils(left_motor, right_motor)
        self.attachment_motor = attachment_motor
        self.drive_base = drive_base

    def run(self):
        self.motor_utils.backwards(300,32)
        self.drive_base.turn(50)
        self.drive_base.turn(70)
        self.motor_utils.backwards(300,20)
        self.drive_base.turn(35)
        self.motor_utils.backwards(300,-22)
        self.attachment_motor.run_angle(1500, 2300)
        self.motor_utils.backwards(300, 48)
