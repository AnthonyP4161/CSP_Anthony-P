import time
import sys
import threading
import os
import random
delay = .01
message1 = "PRESS ENTER TO CONTINUE"


def flashing_text1(stop_event):
    sys.stdout.write("\033[?25l")  # Hide the cursor
    sys.stdout.flush()
    while not stop_event.is_set():
        sys.stdout.write("\rPress ENTER to continue   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r                                ")  # Ensure the line is cleared properly
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\033[?25h")  # Show the cursor again
    sys.stdout.flush()


def start_game():
    
    print("Welcome to my text based adventure.\nYour character will be represented by a [Y]\nRocks which you cannot pass through will be represented by [R]")
    for char in message1:
        print(char, end="", flush=True)
        time.sleep(delay)

    stop_event = threading.Event()
    thread = threading.Thread(target=flashing_text1, args=(stop_event,))
    thread.start()

    input()
    stop_event.set()
    thread.join()
    os.system("cls" if os.name == "nt" else "clear")

player_block =""" \

 [Y]"""

empty = """ \
[ ]"""

rock = """ \
[R]"""

def map_generation():
    quadrant2 = random.randint(1,3)
    quadrant3 = random.randint(1,3)
    quadrant4 = random.randint(1,3)
    quadrant5 = random.randint(1,3)
    quadrant6 = random.randint(1,3)
    quadrant7 = random.randint(1,3)
    quadrant8 = random.randint(1,3)
    quadrant9 = random.randint(1,3)
    quadrant1 = player_block
    if quadrant2 == 3:
        quadrant2 = rock
    else:
        quadrant2 = empty
    if quadrant3 == 3:
        quadrant3 = rock
    else:
        quadrant3 = empty
    if quadrant4 == 3:
        quadrant4 = rock
    else:
        quadrant4 = empty
    if quadrant5 == 3:
        quadrant5 = rock
    else:
        quadrant5 = empty
    if quadrant6 == 3:
        quadrant6 = rock
    else:
        quadrant6 = empty
    if quadrant7 == 3:
        quadrant7 = rock
    else:
        quadrant7 = empty
    if quadrant8 == 3:
        quadrant8 = rock
    else:
        quadrant8 = empty
    if quadrant9 == 3:
        quadrant9 = rock
    else:
        quadrant9 = empty
 

    display_map = print(f"""{quadrant1}{quadrant2}{quadrant3}
{quadrant4}{quadrant5}{quadrant6}
{quadrant7}{quadrant8}{quadrant9}""")
start_game()
map_generation()