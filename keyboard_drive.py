import time
import curses

# import the AStar class from a_star.py
#from a_star import AStar

# Initiate an object from the class AStar
#a=AStar()

# Create a curses screen object 
# (Think of this as your terminal screen)
stdscr=curses.initscr()

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

def keyboard_teleop(stdscr):
    stdscr.clear()

    # Keyboard input timeout loop in milliseconds
    stdscr.timeout(100)

    # Add string on the screen, starting at the (0,0) position or Top left
    stdscr.addstr(0,0,'''
    Use keyboards to drive robot:

          i
       j  k  l
          ,

    q: quit
    ''')

    # Create a continuous while loop
    while True:
        # Get the keyboard input
        c = stdscr.getch()
        # at the position: 
        if c == ord('i'):
            stdscr.addstr(30,0,'input: Go forward   ')

        elif c == ord('j'):
            stdscr.addstr(30,0,'input: Left         ')

        elif c == ord('l'):
            stdscr.addstr(30,0,'input: Right        ')

        elif c == ord(','):
            stdscr.addstr(30,0,'input: Backward      ')

        elif c == ord('k'):
            stdscr.addstr(30,0,'input: Standing still')

        elif c == ord('q'):
            break  # Exit the while loop

    stdscr.refresh()

def main():
    pass

if __name__=="__main__":
    curses.wrapper(keyboard_teleop)

