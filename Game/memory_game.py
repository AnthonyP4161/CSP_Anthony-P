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
    [ x ] [ x ]""",  
  
    f"""  
    [ {memory_2} ] [ {memory_3} ]   
    [ {memory_3} ] [ {memory_1} ]  
    [ {memory_1} ] [ {memory_2} ]""",  
  
    """  
    [ x ] [ x ]    
    [ x ] [ x ]    
    [ x ] [ x ]""",  
    ]  

    for frame in frames:  
        print(frame)  
        time.sleep(1)  # Pause for a moment to show the frame  
        os.system("cls" if os.name == "nt" else "clear")  # Clear the screen  
    return [memory_1, memory_2, memory_3]
def check_guess(user_input, correct_guess):
    if user_input == correct_guess:
        print("Well done!")
    else:
        print("Try again!")
while True:  # Loop until the user guesses correctly  
    correct_sequence = start_game()  # Display the frames and get the correct sequence  
    user_input = input("Please enter your answer: ").split()  
      
    try:  
        user_input = [int(num) for num in user_input]  # Convert user input to integers  
        if check_guess(user_input, correct_sequence):  # Check if the guess is correct  
            break  # Exit the loop if correct  
    except ValueError:  
        print("Please enter numbers only!")  # Handle invalid input 