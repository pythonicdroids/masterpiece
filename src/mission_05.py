from pybricks.tools import wait

class Mission_05:
    def __init__(self, right_color_sensor, left_color_sensor, left_motor, right_motor, attachment_motor):
        self.right_color_sensor = right_color_sensor
        self.left_color_sensor = left_color_sensor
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.attachment_motor = attachment_motor

    #defining the  left and right turns
    def right_turn(self, degree):
        self.left_turn(degree * -1)

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
            if use_right == True and use_left == False:
                if self.right_color_sensor.reflection() < reflection and self.right_color_sensor.reflection() > 70 :
                    self.right_motor.brake()
                    self.left_motor.brake()
                    break

            if use_right == False and use_left == True:
                if self.left_color_sensor.reflection() < reflection and self.left_color_sensor.reflection() > 70 :
                    self.right_motor.brake()
                    self.left_motor.brake()
                    break


    def run(self, run_mission_8 = False):
        self.backwards(250, 49)
        self.left_turn(68)
        self.backwards_until_reflection_black(200, 10, False, True)
        self.left_turn(23)
        self.right_motor.run_time(-300, 5, wait = False)
        self.left_motor.run_time(-300, 5, wait = True)

        if run_mission_8:
            print("TODO: run mission 8")

        self.forward(100, 10)
        self.right_turn(92)
        self.backwards(350, 70)
        self.right_turn(70)
        self.backwards(400, 85)
        
        #backwards_until_reflection_white(200, 90, True, False)
        #right_turn(90)
    