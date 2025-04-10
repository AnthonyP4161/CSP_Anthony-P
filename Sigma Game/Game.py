import os
import sys
import time
import random
import threading
delay = .01
#Selecting difficulty of the game
#Introduction to the game
def instructions():  
    instructions = "Welcome, this is a roguelike trivia game.\nYou will usually be presented with a question, but sometimes there may be a game.\nIf you fail to answer the question correctly or complete the game, you will be forced to restart.\nPlease press enter to begin.\n"
    for char in instructions:
        print(char, end="")
        time.sleep(delay)
    input()
    instructions2 = "Please choose what difficulty you would like.\nEnter 1 for easy, enter 2 for medium, and enter 3 for hard.\n"
    for char in instructions2:
        print(char, end="")
        time.sleep(delay)
instructions()
def difficulty_selection():
    difficulty = int(input("What difficulty would you like: "))
    if difficulty == 1:
        return difficulty
    elif difficulty == 2:
        return difficulty
    elif difficulty == 3:
        return difficulty
    else:
        print("Thats not a valid input!")
        difficulty = difficulty_selection()
        return difficulty
difficulty = difficulty_selection()
print(difficulty) 