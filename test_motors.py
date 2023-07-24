import time

# import the AStar class from a_star.py
from a_star import AStar

# Initiate an object from the class AStar
a=AStar()

# We will use the method "motors"
# to drive Romibot in different dirrection
# a.motors(left_motor_speed,right_motor_speed)
# and define these action in a function

def zero_motor():
    # Set both motors speed to zero, i.e standing still
    a.motors(0,0)

def go_forward(speed):
    # Set both motors to the same speed, i.e moving forward
    a.motors(speed,speed)

def go_backward(speed):
    # Set both motor to negative same speed, i.e moving backward
    a.motors(-speed,-speed)

def rotate_left(speed):
    # Set left motor to go backward, right motor to go forward
    # i.e. rotate left
    a.motors(-speed,speed)

def rotate_right(speed):
    # Set left motor to go forward, right motor to go backward
    # i.e. rotate right
    a.motors(speed,-speed)

def main():
    # Run these action in sequence
    s=200
    d=5
    go_forward(s)
    time.sleep(d)
    zero_motor()
    rotate_left(s)
    time.sleep(d)
    zero_motor()
    rotate_right(s)
    time.sleep(d)
    zero_motor()

if __name__=="__main__":
    main()

