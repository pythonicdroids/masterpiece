from pybricks.tools import wait

class Run_05:
    def __init__(self, left_motor, right_motor, attachment_motor, left_color_sensor, right_color_sensor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.attchment_motor = attachment_motor
        self.left_color_sensor = left_color_sensor
        self.right_color_sensor = right_color_sensor

    #defining the  left and right turns
    def right_turn(self, degree, speed):
        self.left_turn (degree * -1, speed)

    def left_turn(self, degree, speed):
        distance_between_wheels = 143
        pi = 3.14159
        wheel_diameter = 88
        wheel_circumfrence = wheel_diameter * pi
        distance_per_turn_degree = distance_between_wheels * pi / 360
        distance_to_rotate = distance_per_turn_degree * degree
        rotation_angle = distance_to_rotate / wheel_circumfrence * 360

        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        self.left_motor.run_angle(speed,  -rotation_angle,  wait=False)
        self.right_motor.run_angle(speed, rotation_angle,   wait=False) 
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)

    def forward(self, speed, distance_cm):
        circ_cm = 27.6
        self.left_motor.run_angle(speed,  distance_cm/circ_cm * 360, wait = False)
        self.right_motor.run_angle(speed, distance_cm/circ_cm * 360, wait = False)
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)

    def backwards(self, speed, distance_cm):
        self.forward(speed, -distance_cm)

    #align to black lign for light show(only using right motor to detect the color)
    def forward_until_reflection(self, speed, reflection, use_right, use_left ):
        self.left_motor.run_angle(speed, -10000, wait = False)
        self.right_motor.run_angle(speed, 10000, wait = False)
        while True:
            if use_right == True and use_left == False:
                if self.right_color_sensor.reflection() < reflection:
                    self.right_motor.brake()
                    self.left_motor.brake()
                    break

            if use_right == False and use_left == True:
                if self.left_color_sensor.reflection() < reflection:
                    self.right_motor.brake()
                    self.left_motor.brake()
                    break   

    def run(self):
        self.forward(250, 65)
        self.right_turn(84, 100)
        self.forward(300, 69)
        self.left_turn(20, 200)
        self.backwards(300, 15)
        self.right_turn(21, 300)
        self.backwards(400, 57)
        self.right_turn(116, 500)
        self.forward(395, 55)