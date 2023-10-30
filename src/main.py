from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Side, Port, Direction
from pybricks.tools import wait
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from mission_01_10 import Mission_01_10
from mission_05 import Mission_05
from mission_06_07 import Mission_06_07
from mission_11_12 import Mission_11_12

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
right_color_sensor = ColorSensor(Port.F)
left_color_sensor = ColorSensor(Port.B)

mission_01_10 = Mission_01_10(left_motor, right_motor, attachment_motor)
mission_05    = Mission_05(right_color_sensor, left_color_sensor, left_motor, right_motor, attachment_motor)
mission_06_07 = Mission_06_07(drive_base, attachment_motor)
mission_08_09 = Mission_08_09(left_motor, right_motor)
mission_11_12 = Mission_11_12(left_motor, right_motor, attachment_motor)
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
            mission_01_10.mission_one()
        if counter == 2:
            mission_08_09.run()
        if counter == 5:
            mission_05.run(False)
        elif counter == 6:
            mission_06_07.run()
        elif counter == 7:
            mission_11_12.run()
        elif counter == 10:
            mission_01_10.mission_ten()

    elif Button.BLUETOOTH in pressed:
        if counter == 1:
            mission_01_10.mission_one_ten()
        if counter == 5:
            mission_05.run(True)

    # Display the number so we know where we are
    hub.display.number(counter)
    hub.speaker.beep()
