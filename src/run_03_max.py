class Run_03():
    def __init__(self, robot):
        self.robot = robot

    def run(self):
        attachment_motor_speed = 8000
        light_show_turn_angle = 500
        # Need to adjust the distance because the wheel radius is wrong
        distance_ratio = 56 / 88
        self.robot.drive_base.settings(200, 180, 200)
        self.robot.drive_base.straight(930 * distance_ratio) 
        self.robot.drive_base.turn(-85)
        self.robot.drive_base.straight(10 * distance_ratio)
        self.robot.drive_base.turn(-5)
        self.robot.drive_base.straight(85 * distance_ratio)
        # lift the bar in increments to generate more power
        self.robot.attachment_motor.run_angle(attachment_motor_speed, 200 * distance_ratio)
        self.robot.attachment_motor.run_angle(attachment_motor_speed, -100 * distance_ratio)
        self.robot.attachment_motor.run_angle(attachment_motor_speed, 200 * distance_ratio)
        self.robot.attachment_motor.run_angle(attachment_motor_speed, -100 * distance_ratio)
        self.robot.attachment_motor.run_angle(attachment_motor_speed, (light_show_turn_angle - 200) \
                                                     * distance_ratio)
        # use run_time to avoid getting stuck when lower the arms
        self.robot.attachment_motor.run_time(-1000, 800)
        self.robot.drive_base.straight(-115 * distance_ratio)
        self.robot.drive_base.turn(-45)
        self.robot.drive_base.straight(260 * distance_ratio)
        # pick up Noah
        self.robot.side_motor.run_time(150,400)
        self.robot.drive_base.turn(-60)
        self.robot.drive_base.straight(700 * distance_ratio)
        self.robot.side_motor.run_angle(1000, -30 * distance_ratio)
