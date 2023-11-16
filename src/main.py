from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Side, Port, Direction, Icon
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from run_01_kavya import Run_01
from run_02_vivaan import Run_02
from run_03_aron import Run_03
from run_04_aron import Run_04
from run_05_ishanvi import Run_05
from run_06_max import Run_06

# Initialize the hub.
hub = PrimeHub()
# Change the stop button
hub.system.set_stop_button((Button.BLUETOOTH))

hub.display.orientation(Side.LEFT)
counter = 1
hub.display.number(counter)

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E)
attachment_motor = Motor(Port.D)
side_motor = Motor(Port.C)
drive_base = DriveBase(left_motor, right_motor, wheel_diameter = 56, axle_track = 112)
drive_base.settings(200,200,200)
left_color_sensor = ColorSensor(Port.B)
right_color_sensor = ColorSensor(Port.F)

run_01 = Run_01(drive_base, left_motor, right_motor, side_motor)
run_02 = Run_02(left_motor, right_motor, attachment_motor, side_motor)
run_03 = Run_03(left_motor, right_motor, attachment_motor, left_color_sensor, right_color_sensor, side_motor)
run_04 = Run_04(left_motor, right_motor, side_motor)
run_05 = Run_05(left_motor, right_motor, side_motor, attachment_motor, drive_base)
run_06 = Run_06(drive_base, attachment_motor, side_motor)
stop_watch = StopWatch()

def set_gyro(use_gyro):
    print("Setting use_gyro to", use_gyro)
    drive_base.use_gyro(use_gyro)
    if use_gyro:
        hub.display.icon(Icon.TRUE)
    else:
        hub.display.icon(Icon.FALSE)
    wait(500)

use_gyro = True
set_gyro(use_gyro)
stop_watch_reseted = False

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
        else:
            use_gyro = not use_gyro
            set_gyro(use_gyro)

    elif Button.LEFT in pressed:
        counter = counter + 1
    elif Button.CENTER in pressed:
        if counter == 1 and not stop_watch_reseted:
            stop_watch.reset()
            stop_watch_reseted = True
        start_time = stop_watch.time()/1000
        print("Mission ", counter, " starting,  elapsed: \t", start_time)
        if counter == 1:
            # run_01.nudge_lever()
            run_02.mission_one()
        if counter == 2:
            run_01.mission_02()
        if counter == 3:
            run_03.run(True)
        if counter == 4:
            run_04.run()
        elif counter == 5:
            run_05.run2()
        elif counter == 6:
            run_01.push_camera()
        elif counter == 7:
            run_06.run()
        end_time = stop_watch.time()/1000
        print("Mission ", counter, " completed, elapsed: \t", end_time, ", took: ", end_time - start_time)

    # Display the number so we know where we are
    hub.display.number(counter)
    hub.speaker.beep()