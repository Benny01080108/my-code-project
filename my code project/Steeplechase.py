"""
File: Steeplechase.py
Name: TODO:Benny
"""


from karel.stanfordkarel import *

def right():
    for i in range(3):
        turn_left()
    return
def up():
    while not (front_is_clear()):
        turn_left()
        move()
        right()
    move()
    right()
    return
def down():
    while (front_is_clear()):
        move()
    turn_left()
    return


def main():

    for i in range(11):
        if front_is_clear():
            move()
        else:
            up()
            down()





# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
