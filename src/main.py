from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Side, Port, Direction
from pybricks.tools import wait
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from run_01_kavya import Run_01
from run_02_vivaan import Run_02
from run_03_aron import Run_03
from run_04_ishanvi import Run_04
from run_05_aron import Run_05
from run_06_max import Run_06

# Initialize the hub.
hub = PrimeHub()
# Change the stop button
hub.system.set_stop_button((Button.CENTER, Button.BLUETOOTH))

hub.display.orientation(Side.LEFT)
counter = 1
hub.display.number(counter)

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
attachment_motor = Motor(Port.D)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter = 56, axle_track = 112)
drive_base.settings(200,200,200)
left_color_sensor = ColorSensor(Port.B)
right_color_sensor = ColorSensor(Port.F)

run_01 = Run_01(left_motor, right_motor)
run_02 = Run_02(left_motor, right_motor)
run_03 = Run_03(left_motor, right_motor, attachment_motor, left_color_sensor, right_color_sensor)
run_04 = Run_04(left_motor, right_motor, attachment_motor, drive_base)
run_05 = Run_05(left_motor, right_motor, attachment_motor, left_color_sensor, right_color_sensor)
run_06 = Run_06(drive_base, attachment_motor)
# Wait for any button to be pressed
while True:
    pressed = []
    while not any(pressed):
        pressed = hub.buttons.pressed()
        wait(100)
    while any(hub.buttons.pressed()):
        wait(100)

    if Button.RIGHT in pressed:
        if counter > 1:
            counter = counter - 1
    elif Button.LEFT in pressed:
        counter = counter + 1
    elif Button.CENTER in pressed:
        if counter == 1:
            run_01.nudge_lever()
        if counter == 2:
            run_02.mission_one()
        if counter == 3:
            run_03.run(False)
        if counter == 4:
            run_04.run()
        elif counter == 5:
            run_05.run()
        elif counter == 6:
            run_06.run()

    elif Button.BLUETOOTH in pressed:
        if counter == 1:
            run_01.mission_02()
        if counter == 3:
            run_03.run(True)
        if counter == 6:
            run_01.push_camera()

    # Display the number so we know where we are
    hub.display.number(counter)
    hub.speaker.beep()
