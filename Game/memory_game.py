# Anthony Memory

import time
import os
import random
ANuser_input = "nothing"
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
        os.system("cls" if os.name == "nt" else "clear")  # Clear the screen
    return [ANmemory_2, ANmemory_3, ANmemory_3, ANmemory_1, ANmemory_1, ANmemory_2]
def check_guess(ANuser_input, ANcorrect_guess):
    if ANuser_input == ANcorrect_guess:
        print("Well done!")
        return("Well done!")
    else:
        print("Try again!")
    
print("This is a memory game that will flash the numbers and you have to repeat them.")
ANBegin = input("Please type yes to begin: ")
if ANBegin == "yes":
    while True:  # Loop until the user guesses correctly
        ANcorrect_sequence = start_game()  # Display the frames and get the correct sequence
        ANuser_input = input("Please enter your answer, and remember to add spaces in between each number: ").split()  
      
        try:  
            ANuser_input = [int(num) for num in ANuser_input]  # Convert input to integers
            if check_guess(ANuser_input, ANcorrect_sequence) == "Well done!":  # Check if the guess is correct
                break  # Exit the loop if correct
        except ValueError:  
            print("Please enter numbers only!")  #If someone enters letters