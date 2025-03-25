# Anthony Memory

import time
import os
import random
user_input = "nothing"
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
    print(frames)
    time.sleep(1)  # Adjust speed if needed'
    os.system("cls" if os.name == "nt" else "clear")  # Clears screen for smooth animation
    user_input = input("Please enter your answer: ").split()
    return [memory_1, memory_2, memory_3]
def check_guess(user_input, correct_guess):
    if user_input == correct_guess:
        print("Well done!")
    else:
        print("Try again!")
start_game()
correct_sequence = start_game()
check_guess(user_input, correct_sequence)