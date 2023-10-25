from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Side, Port, Direction
from pybricks.tools import wait
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.robotics import DriveBase
from mission_1_10 import Mission_1_10
from mission_5 import Mission_5
from mission_6_7 import Mission_6_7
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

mission_1_10 = Mission_1_10(left_motor, right_motor, attachment_motor)
mission_5 = Mission_5(right_color_sensor, left_color_sensor, left_motor, right_motor, attachment_motor)
mission_6_7 = Mission_6_7(drive_base, attachment_motor)
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
            mission_1_10.mission_one()
        if counter == 5:
            mission_5.run(False)
        elif counter == 6:
            mission_6_7.run()
        elif counter == 7:
            mission_11_12.run()
        elif counter == 10:
            mission_1_10.mission_ten()

    elif Button.BLUETOOTH in pressed:
        if counter == 1:
            mission_1_10.mission_one_ten()
        if counter == 5:
            mission_5.run(True)

    # Display the number so we know where we are
    hub.display.number(counter)
    hub.speaker.beep()
