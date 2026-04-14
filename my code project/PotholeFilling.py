"""
File: PotholeFilling.py
Name: TODO:Benny
--------------------------
"""
from karel.stanfordkarel import *
def put():
    for i in range(99):
        put_beeper()

def right():
    for i in range(3):
        turn_left()
    return
def go_out():
    for i in range(2):
        turn_left()
    move()
    right()
def goin():
    for i in range(2):
        move()
    right()
    move()
    put()
def main():
    move()
    right()
    move()
    put()
    go_out()
    for i in range(2):
        goin()
        go_out()

    move()


if __name__ == '__main__':
    execute_karel_task(main)
