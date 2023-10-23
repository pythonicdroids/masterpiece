from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.pupdevices import ColorSensor
from pybricks.tools import wait
from pybricks.geometry import Axis

hub = PrimeHub()
right_color_sensor = ColorSensor(Port.F)
left_color_sensor = ColorSensor(Port.B)
left_motor = Motor(Port.A)
right_motor = Motor(Port.E)
attachment_motor = Motor(Port.D)

#defining the  left and right turns
def right_turn(degree):
    left_turn (degree * -1)

def left_turn(degree):
    distance_between_wheels = 143
    pi = 3.14159
    wheel_diameter = 88
    wheel_circumfrence = wheel_diameter * pi
    distance_per_turn_degree = distance_between_wheels * pi / 360
    distance_to_rotate = distance_per_turn_degree * degree
    rotation_angle = distance_to_rotate / wheel_circumfrence * 360

    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_angle(300,  rotation_angle,  wait=False)
    right_motor.run_angle(300, rotation_angle,   wait=False) 
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
def forward_until_reflection_black(speed, reflection, use_right, use_left ):
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

def backwards_until_reflection_black(speed, reflection, use_right, use_left ):
   left_motor.run_angle(speed, 10000, wait = False)
   right_motor.run_angle(speed, -10000, wait = False)
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

def backwards_until_reflection_black(speed, reflection, use_right, use_left ):
   left_motor.run_angle(speed, 10000, wait = False)
   right_motor.run_angle(speed, -10000, wait = False)
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

def backwards_until_reflection_white(speed, reflection, use_right, use_left ):
   left_motor.run_angle(speed, 10000, wait = False)
   right_motor.run_angle(speed, -10000, wait = False)
   while True:
      if use_right == True and use_left == False:
         if right_color_sensor.reflection() < reflection and right_color_sensor.reflection() > 70 :
            right_motor.brake()
            left_motor.brake()
            break

      if use_right == False and use_left == True:
         if left_color_sensor.reflection() < reflection and left_color_sensor.reflection() > 70 :
            right_motor.brake()
            left_motor.brake()
            break

doing_mission8 = True



backwards(250, 49)
left_turn(68)
backwards_until_reflection_black(200, 10, False, True)
left_turn(23)
right_motor.run_time(-300, 5, wait = False)
left_motor.run_time(-300, 5, wait = False)
forward(100, 10)
right_turn(92)
backwards(350, 70)
right_turn(70)
backwards(400, 85)
   
#backwards_until_reflection_white(200, 90, True, False)
#right_turn(90)
   










