"""
TODO: Benny
--------------------
"""



from karel.stanfordkarel import *

def right():
    for i in range(3):
        turn_left()
    return

def around():
    for i in range(2):
        turn_left()
    return




def main():
    print('w=forward,s=back,r=right,l=left')
    print('NO.1 beeper is a bomb and NO.99 beeper is a finish point')
    print('good luck for you to win the game')
    turn_left()
    while(1):
        a=input('please move:')
        if a=='w':
            move()
        elif a=='s':
            around()
        elif a=='r':
            right()
        elif a=='l':
            turn_left()

        if on_beeper():
            if facing_east()and (not front_is_clear())and (not left_is_clear()):
                print('you win')
            elif facing_north()and (not front_is_clear())and (not right_is_clear()):
                print('you win')
            else:
                pick_beeper()
                print('Game over')

            break


if __name__ == '__main__':
    execute_karel_task(main)
