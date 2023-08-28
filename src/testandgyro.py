from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.tools import wait
from pybricks.parameters import Port
hub = PrimeHub()
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)
wheel_distance = 128
rotation_per_distance = 276
rotation_per_turn = wheel_distance * 3.14159 / 360
for i in range(20):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_angle(300, -200*rotation_per_distance, wait=False)
    right_motor.run_angle(300, 200*rotation_per_distance, wait=False)
    while not left_motor.done() or not right_motor.done():
        wait(10)
    left_motor.run_angle(300,  90*rotation_per_turn*rotation_per_distance, wait=False)
    right_motor.run_angle(300, 90*rotation_per_turn*rotation_per_distance, wait=False)
    while not left_motor.done() or not right_motor.done():
        wait(10)

