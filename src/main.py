from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initizlie the hub.
hub = PrimeHub()

hub.display.text("Hello, world!!!")

# Testing motor movements
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)

left_motor.run_angle(500, 500, wait=False)
right_motor.run_angle(500, -500, wait=False)

while not left_motor.done() or not right_motor.done():
   wait(10)

print("Both motors are done!")