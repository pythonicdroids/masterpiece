from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initizlie the hub.
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)
hub = PrimeHub()
def forward(speed,distance):
   c_cm = 27.6
   left_motor.run_angle(speed, -distance/c_cm * 360, wait=False)
   right_motor.run_angle(speed, distance/c_cm * 360, wait=False)
   while not left_motor.done() or not right_motor.done():
      wait(10)