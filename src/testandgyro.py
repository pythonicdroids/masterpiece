from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.tools import wait
from pybricks.parameters import Port
hub = PrimeHub()
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)
for i in range(20):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_angle(300, -200, wait=False)
    right_motor.run_angle(300, 200, wait=False)
    while not left_motor.done() or not right_motor.done():
        wait(10)
    left_motor.run_angle(300,  148, wait=False)
    right_motor.run_angle(300, 148, wait=False)
    while not left_motor.done() or not right_motor.done():
        wait(10)

