from pybricks.tools import wait
from mission_base import MissionBase

class Run_03(MissionBase):
    def __init__(self, left_motor, right_motor, attachment_motor, left_color_sensor, right_color_sensor):
        super().__init__(left_motor, right_motor)
        self.attachment_motor = attachment_motor
        self.left_color_sensor = left_color_sensor
        self.right_color_sensor = right_color_sensor

    #align to black lign for light show(only using right motor to detect the color)
    def forward_until_reflection_black(self, speed, reflection, use_right, use_left ):
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        self.left_motor.run_angle(speed,  10000, wait = False)
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
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        self.left_motor.run_angle(speed, -10000, wait = False)
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
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        self.left_motor.run_angle(speed, -10000, wait = False)
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
        self.left_turn(300, 68)
        self.backwards_until_reflection_black(300, 10, False, True)
        self.left_turn(300, 21)
        self.right_motor.run_time(-160, 2200, wait = False)
        self.left_motor.run_time(-160, 2200, wait = True)
        wait(10)
        self.left_turn(300, 7)

        if doing_mission7 == True:
            # going back from finishing mission 5
            self.forward(100, 15)
            self.left_turn(300, 94)
            self.right_motor.run_time(340, 3000, wait = False)
            self.left_motor.run_time(340, 3000, wait = True)
            self.left_turn(300, 20)
            self.right_motor.run_time(140, 1500, wait = False)
            self.left_motor.run_time(140, 1500, wait = True)
            self.backwards(400, 10)
            wait(10)
            self.left_turn(300, 90)
            self.backwards(400, 70)
            
        else:
            self.forward(100, 10)
            self.right_turn(300, 92)
            self.backwards(400, 70)
            self.right_turn(300, 60)
            self.backwards(600, 100)