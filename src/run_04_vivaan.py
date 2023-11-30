from pybricks.tools import wait

class Run_04():
    def __init__(self, robot):
        self.robot = robot

    def frontmotor(self, speed, degree, wait_for_turn):
        distance_between_wheels = 143
        pi = 3.14159
        wheel_diameter = 88
        wheel_circumfrence = wheel_diameter * pi
        distance_per_turn_degree = distance_between_wheels * pi / 360
        wait(10)
        distance_to_rotate = distance_per_turn_degree * degree
        rotation_angle = distance_to_rotate / wheel_circumfrence * 360
        self.robot.attachment_motor.reset_angle(0)
        self.robot.attachment_motor.run_angle(speed,  rotation_angle, wait=wait_for_turn) 

    def mission_one_two_ten(self):
        self.robot.drive_base.straight(230)
        self.robot.drive_base.straight(-20)
        self.frontmotor(1800, 1500, True)
        # turn in small increments to make sure we don't miss the middle knob
        self.robot.drive_base.turn(5)
        self.robot.drive_base.turn(5)
        wait(500)
        self.robot.drive_base.turn(10)
        # back out
        self.robot.drive_base.straight(-50)
        self.robot.drive_base.turn(-90)
        # curve to skate park
        self.robot.drive_base.curve(180, 90)
        # drop Izzie and audience member
        self.robot.side_motor.run_angle(100, -80)
        self.robot.drive_base.straight(-50)
        # slow down the turn to prevent over turn
        self.robot.drive_base.settings(100, 200, 200)
        self.robot.drive_base.turn(-70)
        self.robot.drive_base.settings(200, 200, 200)
        self.robot.drive_base.straight(50)
        # pick up Sam
        self.robot.side_motor.run_angle(200, 90)
        self.robot.drive_base.straight(-90)
        self.robot.drive_base.turn(-35)
        # push theater scene change
        self.robot.drive_base.straight(60)
        # lower front wedge
        self.frontmotor(1800, -1050, False)
        self.robot.drive_base.curve(-120, -80)
        self.robot.drive_base.straight(-330)
        self.robot.drive_base.turn(-50)
        self.robot.drive_base.straight(170)
        # nodge 3D cinema
        self.robot.drive_base.turn(30)
        self.robot.drive_base.straight(-180)
        self.frontmotor(1800, -450, True)

    def mission_10(self):
        self.robot.drive_base.straight(250)
        self.robot.drive_base.straight(-15)
        self.robot.attachment_motor.run_angle(3000, -340)
        self.robot.drive_base.turn(5)
        wait(500)
        self.robot.drive_base.straight(-37)
        self.robot.attachment_motor.run_angle(30000, 340)


        #turn like 90
        #forward
        #turn
        #backwards
