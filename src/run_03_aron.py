from pybricks.tools import wait

class Run_03:
    def __init__(self, left_motor, right_motor, attachment_motor, left_color_sensor, right_color_sensor):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.attachment_motor = attachment_motor
        self.left_color_sensor = left_color_sensor
        self.right_color_sensor = right_color_sensor

    def right_turn(self, degree):
        self.left_turn (degree * -1)

    def left_turn(self, degree):
        distance_between_wheels = 143
        pi = 3.14159
        wheel_diameter = 88
        wheel_circumfrence = wheel_diameter * pi
        distance_per_turn_degree = distance_between_wheels * pi / 360
        distance_to_rotate = distance_per_turn_degree * degree
        rotation_angle = distance_to_rotate / wheel_circumfrence * 360

        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        self.left_motor.run_angle(300,  rotation_angle,  wait=False)
        self.right_motor.run_angle(300, rotation_angle,   wait=False) 
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)

    def forward(self, speed, distance_cm):
        circ_cm = 27.6
        self.left_motor.run_angle(speed, -distance_cm/circ_cm * 360, wait = False)
        self.right_motor.run_angle(speed, distance_cm/circ_cm * 360, wait = False)
        while not self.left_motor.done() or not self.right_motor.done():
            wait(10)

    def backwards(self, speed, distance_cm):
        self.forward(speed, -distance_cm)

    #align to black lign for light show(only using right motor to detect the color)
    def forward_until_reflection_black(self, speed, reflection, use_right, use_left ):
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

    def backwards_until_reflection_black(self, speed, reflection, use_right, use_left ):
        self.left_motor.run_angle(speed, 10000, wait = False)
        self.right_motor.run_angle(speed, -10000, wait = False)
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

    def backwards_until_reflection_black(self, speed, reflection, use_right, use_left ):
        self.left_motor.run_angle(speed, 10000, wait = False)
        self.right_motor.run_angle(speed, -10000, wait = False)
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

    def backwards_until_reflection_white(self, speed, reflection, use_right, use_left ):
        self.left_motor.run_angle(speed, 10000, wait = False)
        self.right_motor.run_angle(speed, -10000, wait = False)
        while True:
            print(self.right_color_sensor.reflection())
            wait(500)
            if use_right == True and use_left == False:
                if self.right_color_sensor.reflection() < reflection and self.right_color_sensor.reflection() > 56 :
                    self.right_motor.brake()
                    self.left_motor.brake()
                    break

            if use_right == False and use_left == True:
                if self.left_color_sensor.reflection() < reflection and self.left_color_sensor.reflection() > 56 :
                    self.right_motor.brake()
                    self.left_motor.brake()
                    break

    def run(self, doing_mission7):
        self.backwards(300, 51)
        self.left_turn(68)
        self.backwards_until_reflection_black(300, 10, False, True)
        self.left_turn(21)
        self.right_motor.run_time(-180, 2200, wait = False)
        self.left_motor.run_time(180, 2200, wait = True)
        wait(10)
        self.left_turn(2)

        if doing_mission7 == True:
            # self.backwards(270, 50)
            # self.left_turn(68)
            # self.backwards_until_reflection_black(200, 10, False, True)
            # self.left_turn(21)
            # self.right_motor.run_time(-180, 2200, wait = False)
            # self.left_motor.run_time(180, 2200, wait = True)
            # wait(10)
            # self.left_turn(3)
            self.forward(100, 18)
            self.left_turn(94)
            self.right_motor.run_time(340, 3000, wait = False)
            self.left_motor.run_time(-340, 3000, wait = True)
            self.left_turn(20)
            self.right_motor.run_time(140, 1500, wait = False)
            self.left_motor.run_time(-140, 1500, wait = True)
            self.backwards(400, 10)
            wait(10)
            self.left_turn(90)
            self.backwards(400, 70)
        else:
            # self.backwards(270, 50)
            # self.left_turn(68)
            # self.backwards_until_reflection_black(200, 10, False, True)
            # self.left_turn(21)
            # self.right_motor.run_time(-180, 2200, wait = False)
            # self.left_motor.run_time(180, 2200, wait = True)
            # wait(10)
            # self.left_turn(3)
            self.forward(100, 10)
            self.right_turn(95)
            self.backwards(400, 70)
            self.right_turn(70)
            self.backwards(600, 100)