from motor_utils import MotorUtils

class Mission_11_12:
    def __init__(self, left_motor, right_motor, attachment_motor):
        self.motor_utils = MotorUtils(left_motor, right_motor)
        self.attachment_motor = attachment_motor

    def run(self):
        self.motor_utils.forward(300, 48)
        self.front_attachment_motor.run_angle(1500, 2300)
        self.motor_utils.backwards(300, 50)