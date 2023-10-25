from pybricks.tools import wait

class MotorUtils:
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def forward(self, speed, distance_cm):
        wheel_distance = 128
        rotation_per_distance = 276
        rotation_per_turn = wheel_distance * 3.14159 / 360
        circ_cm = 27.6
        self.left_motor.run_angle(speed, -distance_cm/circ_cm * 360, wait = False)
        self.right_motor.run_angle(speed, distance_cm/circ_cm * 360, wait = False)
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)

    def backwards(self, speed, distance_cm):
        self.forward(speed, -distance_cm)