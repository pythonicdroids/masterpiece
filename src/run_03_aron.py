from pybricks.tools import wait
from mission_base import MissionBase

class Run_03(MissionBase):
    def __init__(self, left_motor, right_motor, side_motor, attachment_motor, drive_base, left_color_sensor, right_color_sensor):
        super().__init__(left_motor, right_motor, side_motor)
        self.attachment_motor = attachment_motor
        self.left_color_sensor = left_color_sensor
        self.right_color_sensor = right_color_sensor
        self.drive_base = drive_base
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

    
    def turn_until_right(self, speed, heading_val):
        right_motor.run_angle(speed, 10000, wait = False)
        left_motor.run_angle(speed, -10000, wait = False)
        while True:
            if imu.heading() == heading_val:
                self.right_motor.brake()
                self.left_motor.brake()
                break

    def run(self, doing_mission7):

        self.drive_base.curve(500, -90)
        # Finished mission 3
        # Going to mission 7 and deliver Audience / Expert
        self.drive_base.straight(-50)
        self.drive_base.turn(90)
        self.drive_base.straight(370)
        self.drive_base.turn(-39)
        self.drive_base.straight(75)
        # Getting ready to drop Audience / Expert
        self.side_motor.run_angle(200, -80)
        self.drive_base.straight(-70)
        self.side_motor.run_angle(200, 80)
        # Moved attachement back up so doesn't interfere
        self.drive_base.turn(80)
        self.drive_base.straight(500)






        # self.drive_base.turn(-150)
        # self.drive_base.straight(-100)
        # # Geting ready to do mission 7
        # self.drive_base.turn(-29)
        # self.drive_base.straight(-200)
        # # Finished mission 7
        # # Returning to home area
        # self.drive_base.straight(50)
        # self.drive_base.turn(-90)
        # self.drive_base.straight(500)
        # # Finished the run!!!!!!!!!!

        


