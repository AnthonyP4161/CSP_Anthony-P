import os
import sys
import time
import random
import threading
delay = .01
#Selecting difficulty of the game
def difficulty_selection(gamemode):
    return int(input("Before you begin, please enter the difficulty you would like to choose for your game.\nEnter 1 for easy, 2 for medium, or 3 for hard.\n"))


#Introduction to the game
def instructions():
    instructions = "Welcome, this is a roguelike trivia game.\nYou will usually be presented with a question, but sometimes there may be a game.\nIf you fail to answer the question correctly or complete the game, you will be forced to restart.\nPlease press enter to begin.\n"
    for char in instructions:
        print(char, end="")
        time.sleep(delay)
    input()
instructions()
difficulty_selection()