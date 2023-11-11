from pybricks.tools import wait

class MissionBase:
    def __init__(self, left_motor, right_motor, side_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.side_motor = side_motor

    def forward(self, speed, distance_cm):
        circ_cm = 27.6
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        self.left_motor.run_angle(speed,  distance_cm/circ_cm * 360, wait = False)
        self.right_motor.run_angle(speed, distance_cm/circ_cm * 360, wait = False)
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)
        self.stop()

    def backwards(self, speed, distance_cm):
        self.forward(speed, -distance_cm)
        
    def left_turn(self, degree, speed = 300):
        distance_between_wheels = 143
        pi = 3.14159
        wheel_diameter = 88
        # calculating the wheel circumfrence - wheel diameter multiplied by pi
        wheel_circumfrence = wheel_diameter * pi
        # calculating the distance the wheel needs to spin
        distance_to_rotate = distance_between_wheels * pi / 360 * degree 
        # calculating how many times the wheel needs to turn, and then converts it to degrees
        rotation_angle = distance_to_rotate / wheel_circumfrence * 360
        #reset_angle after every movementt makes the robot's movements more accurate
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        self.left_motor.run_angle(speed,  -rotation_angle,  wait=False)
        self.right_motor.run_angle(speed, rotation_angle,   wait=False) 
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)
        self.stop()

    def stop(self):
        self.left_motor.stop()
        self.right_motor.stop()

    def right_turn(self, degree, speed = 300):
        self.left_turn(degree * -1, speed)
