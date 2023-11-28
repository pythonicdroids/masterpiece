from pybricks.tools import wait
from robot import Robot

class Run_06():
    def __init__(self, robot):
        self.robot = robot
    #align to black lign for light show(only using right motor to detect the color)
    def forward_until_reflection_black(self, speed, reflection, use_right, use_left ):
        self.robot.left_motor.reset_angle(0)
        self.robot.right_motor.reset_angle(0)
        self.robot.left_motor.run_angle(speed,  10000, wait = False)
        self.robot.right_motor.run_angle(speed, 10000, wait = False)
        while True:
            if use_right == True and use_left == False:
                if self.robot.right_color_sensor.reflection() < reflection:
                    self.robot.right_motor.brake()
                    self.robot.left_motor.brake()
                    break

            if use_right == False and use_left == True:
                if self.robot.left_color_sensor.reflection() < reflection:
                    self.robot.right_motor.brake()
                    self.robot.left_motor.brake()
                    break   

    def backwards_until_reflection_black(self, speed, reflection, use_right, use_left ):
        self.robot.left_motor.reset_angle(0)
        self.robot.right_motor.reset_angle(0)
        self.robot.left_motor.run_angle(speed, -10000, wait = False)
        self.robot.right_motor.run_angle(speed, -10000, wait = False)
        while True:
            if use_right == True and use_left == False:
                if self.robot.right_color_sensor.reflection() < reflection:
                    self.robot.right_motor.brake()
                    self.robot.left_motor.brake()
                    break

            if use_right == False and use_left == True:
                if self.robot.left_color_sensor.reflection() < reflection:
                    self.robot.right_motor.brake()
                    self.robot.left_motor.brake()
                    break

    def backwards_until_reflection_white(self, speed, reflection, use_right, use_left ):
        self.robot.left_motor.reset_angle(0)
        self.robot.right_motor.reset_angle(0)
        self.robot.left_motor.run_angle(speed, -10000, wait = False)
        self.robot.right_motor.run_angle(speed, -10000, wait = False)
        while True:
            print(self.robot.right_color_sensor.reflection())
            wait(500)
            if use_right == True and use_left == False:
                if self.robot.right_color_sensor.reflection() < reflection and self.robot.right_color_sensor.reflection() > 56 :
                    self.robot.right_motor.brake()
                    self.robot.left_motor.brake()
                    break

            if use_right == False and use_left == True:
                if self.robot.left_color_sensor.reflection() < reflection and self.robot.left_color_sensor.reflection() > 56 :
                    self.robot.right_motor.brake()
                    self.robot.left_motor.brake()
                    break

    
    def turn_until_right(self, speed, heading_val):
        self.right_motor.run_angle(speed, 10000, wait = False)
        self.left_motor.run_angle(speed, -10000, wait = False)
        while True:
            if self.imu.heading() == heading_val:
                self.robot.right_motor.brake()
                self.robot.left_motor.brake()
                break

    def run(self):

        self.robot.drive_base.curve(500, -90)
        # Finished mission 3
        # Going to mission 7 and deliver Audience / Expert
        self.robot.drive_base.straight(-50)
        self.robot.drive_base.turn(90)
        self.robot.drive_base.straight(370)
        self.robot.drive_base.turn(-39)
        self.robot.drive_base.straight(75)
        # Getting ready to drop Audience / Expert
        self.robot.side_motor.run_angle(200, -80)
        self.robot.drive_base.straight(-70)
        self.robot.side_motor.run_angle(200, 80)
        # Moved attachement back up so doesn't interfere
        self.robot.drive_base.turn(80)
        self.robot.drive_base.straight(500)






        # self.robot.drive_base.turn(-150)
        # self.robot.drive_base.straight(-100)
        # # Geting ready to do mission 7
        # self.robot.drive_base.turn(-29)
        # self.robot.drive_base.straight(-200)
        # # Finished mission 7
        # # Returning to home area
        # self.robot.drive_base.straight(50)
        # self.robot.drive_base.turn(-90)
        # self.robot.drive_base.straight(500)
        # # Finished the run!!!!!!!!!!

        


