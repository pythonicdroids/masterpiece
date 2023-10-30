from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait

hub = PrimeHub()
right_color_sensor = ColorSensor(Port.F)
left_color_sensor = ColorSensor(Port.B)
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)
attachment_motor = Motor(Port.D)

#defining the  left and right turns
def right_turn(degree, speed):
    left_turn (degree * -1, speed)

def left_turn(degree, speed):
    distance_between_wheels = 143
    pi = 3.14159
    wheel_diameter = 88
    wheel_circumfrence = wheel_diameter * pi
    distance_per_turn_degree = distance_between_wheels * pi / 360
    distance_to_rotate = distance_per_turn_degree * degree
    rotation_angle = distance_to_rotate / wheel_circumfrence * 360

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_angle(speed,  rotation_angle,  wait=False)
    right_motor.run_angle(speed, rotation_angle,   wait=False) 
    while not left_motor.done() or not right_motor.done():
        wait(10)

def forward(speed, distance_cm):
   circ_cm = 27.6
   left_motor.run_angle(speed, -distance_cm/circ_cm * 360, wait = False)
   right_motor.run_angle(speed, distance_cm/circ_cm * 360, wait = False)
   while not left_motor.done() or not right_motor.done():
      wait(10)

def backwards(speed, distance_cm):
   forward(speed, -distance_cm)

#align to black lign for light show(only using right motor to detect the color)
def forward_until_reflection(speed, reflection, use_right, use_left ):
   left_motor.run_angle(speed, -10000, wait = False)
   right_motor.run_angle(speed, 10000, wait = False)
   while True:
      if use_right == True and use_left == False:
         if right_color_sensor.reflection() < reflection:
            right_motor.brake()
            left_motor.brake()
            break

      if use_right == False and use_left == True:
         if left_color_sensor.reflection() < reflection:
            right_motor.brake()
            left_motor.brake()
            break   

print("testing, testing")
forward(250, 65)
right_turn(84, 100)
forward(300, 69)
left_turn(20, 200)
backwards(300, 15)
right_turn(21, 300)
backwards(400, 57)
right_turn(116, 500)
forward(395, 55)












