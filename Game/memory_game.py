# Anthony Memory

import time
import os
import random
delay = 0.02
ANuser_input = "nothing"
ANinstructions = "This is a memory game that will display numbers\nIt is your job to remember them and repeat them\n" \
"Please press enter to begin \n"
ANinstructions2 = "Please enter your answer, and remember to add spaces in between each number: \n"
def start_game():
    ANmemory_1 = random.randint(1,9)
    ANmemory_2 = random.randint(1,9)
    ANmemory_3 = random.randint(1,9)
    ANframes = [  
    """  
    [ x ] [ x ]
    [ x ] [ x ]  
    [ x ] [ x ]""",  
  
    f"""  
    [ {ANmemory_2} ] [ {ANmemory_3} ]   
    [ {ANmemory_3} ] [ {ANmemory_1} ]  
    [ {ANmemory_1} ] [ {ANmemory_2} ]""",  
  
    """  
    [ x ] [ x ]    
    [ x ] [ x ]    
    [ x ] [ x ]""",  
    ]  

    for frame in ANframes:  
        print(frame)  
        time.sleep(1)  # Pause for a moment to show the frame
        print("\033[F\033[K" * len(ANframes))
    return [ANmemory_2, ANmemory_3, ANmemory_3, ANmemory_1, ANmemory_1, ANmemory_2]
def check_guess(ANuser_input, ANcorrect_sequence):
    if ANuser_input == ANcorrect_sequence:
        print("Well done!")
        return("Well done!")
    else:
        print("Try again")
for char in ANinstructions:
    print(char, end="")
    time.sleep(delay)
while True:
    if input() == "":
        break
    else:
        continue
ANcorrect_sequence = start_game()  # Display the frames and get the correct sequence
for char in ANinstructions2:
    print(char, end="")
    time.sleep(delay)
while True:  
    ANuser_input = input("Enter your guess here: ")  # Collect input here  
    ANuser_input = [int(num) for num in ANuser_input.split()]  # Convert to list of integers  
  
    if check_guess(ANuser_input, ANcorrect_sequence) == "Well done!": 
        break  # Exit loop if correct
while True:  # Loop until the user guesses correctly
    ANcorrect_sequence = start_game()  # Display the frames and get the correct sequence
    for char in ANinstructions2:
        print(char, end="")
        time.sleep(delay)
        for char in ANinstructions2:
            print(char, end="")
            time.sleep(delay)
        while True:  
            ANuser_input = input("Enter your guess here: ")  # Collect input here  
            ANuser_input = [int(num) for num in ANuser_input.split()]  # Convert to list of integers  
  
            if check_guess(ANuser_input, ANcorrect_sequence) == "Well done!": 
                break  # Exit loop if correct
            else:
                continue
        try:
            ANuser_input = [int(num) for num in ANuser_input]  # Convert input to integers
        except ValueError:  
            print("Please enter numbers only!")  #If someone enters letters