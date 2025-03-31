import time
import sys
import threading
import os
import random
player_block = """
[   ()  ]
[  -||- ]
[  _||_ ]"""

empty = """
[       ]
[       ]
[       ]"""

rock = """
[  ___  ]
[ |   | ]
[ |   | ]"""


def map_generation():
    quadrant1 = random.randint(1,4)
    quadrant2 = random.randint(1,4)
    quadrant3 = random.randint(1,4)
    quadrant4 = random.randint(1,4)
    quadrant5 = random.randint(1,4)
    quadrant6 = random.randint(1,4)
    quadrant7 = random.randint(1,4)
    quadrant8 = random.randint(1,4)
    quadrant9 = random.randint(1,4)
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
    print(player_block, quadrant1, quadrant2,
          quadrant3)
map_generation()