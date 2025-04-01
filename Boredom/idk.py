import time
import sys
import threading
import os
import random
def start_game():
    print("Welcome to my text based adventure. The map will be printed and you will be represented by a [Y], rocks which you cannot")
map = "nothing"
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
    display_map = """{quadrant1} {quadrant2} """
    map = print(display_map)
map_generation()