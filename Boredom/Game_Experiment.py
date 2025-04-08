import random
import os
import time
import sys
import threading

#Map design
player_block = " [ Y ] "
blocked_path = " [ R ] "
empty_path = " [   ] "
goal_block = " [ G ] "


#maps
def map1():
    quadrant1 = player_block
    quadrant2 = empty_path
    quadrant3 = blocked_path
    quadrant4 = blocked_path
    quadrant5 = empty_path
    quadrant6 = empty_path
    quadrant7 = blocked_path
    quadrant8 = blocked_path
    quadrant9 = goal_block

#map generation
def map_generation(map):
    print(map)

map_generation(map1)