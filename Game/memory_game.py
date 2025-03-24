# Anthony Memory

import time
import os
import random

def start_game():
    print("This is a memory game that will flash the numbers and you have to repeat them.")
    memory_1 = random.randint(1,6)
    memory_2 = random.randint(1,6)
    memory_3 = random.randint(1,6)
    frames = [
        """  
        [ x ] [ x ] 
        [ x ] [ x ]
        [ x ] [ x ]
        """,

        f"""
        [ {memory_2} ] [ {memory_3} ] 
        [ {memory_3} ] [ {memory_1} ]
        [ {memory_1} ] [ {memory_2} ]
        """,

        """  
        [ x ] [ x ]  
        [ x ] [ x ]  
        [ x ] [ x ]
        """,
        ]
    while input("Type yes to start the game, or type your answer: ") == "yes" or input != (memory_1, memory_2, memory_3, memory_2, memory_1, memory_3):
        os.system("cls" if os.name == "nt" else "clear")  # Clears screen for smooth animation
        print(frames)
        time.sleep(1)  # Adjust speed if needed'
    return [memory_1, memory_2, memory_3]
def check_guess(user_input, correct_guess):
    if user_input == correct_guess:
        print("Well done!")
    else:
        print("Try again!")
start_game
correct_sequence = start_game
user_input = input("Please enter your answer: ").split()
check_guess(user_input, correct_sequence)