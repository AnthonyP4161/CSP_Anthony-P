import time
import sys
import threading
import os
import random
map = "nothing"
player_block =""" \
[Y]"""


empty = """ \
[ ]"""

rock = """ \
[R]"""

def map_generation():
    quadrant1 = random.randint(1,3)
    quadrant2 = random.randint(1,3)
    quadrant3 = random.randint(1,3)
    quadrant4 = random.randint(1,3)
    quadrant5 = random.randint(1,3)
    quadrant6 = random.randint(1,3)
    quadrant7 = random.randint(1,3)
    quadrant8 = random.randint(1,3)
    if quadrant1 == 3:
        quadrant1 = rock
    else:
        quadrant1 = empty
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
    map = print(player_block, quadrant1, quadrant2,"\n",
          quadrant3, quadrant4, quadrant5)
map_generation()