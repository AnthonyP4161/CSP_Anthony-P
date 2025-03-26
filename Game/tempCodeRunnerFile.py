# Anthony Memory

import time
import os
import random
delay = 0.02
ANuser_input = "nothing"
ANinstructions = "This is a memory game that will display numbers\nIt is your job to remember them and repeat them\n" \
"Please press enter to begin \n"
ANinstructions2 = "Please enter your answer, and remember to add spaces in between each number: \n"
ANinstructions3 = "Please press enter to display the numbers again.\n" \
"NOTE: THE NUMBERS WILL BE DIFFERENT THIS TIME!"
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
        return True
    else:
        print("Try again")
        return False
for char in ANinstructions:
    print(char, end="")
    time.sleep(delay)
while True:
    if input() == "":
        break
    else:
        continue

while True:   
    ANcorrect_sequence = start_game()
        
    print(ANinstructions2, end="")
    ANuser_input = input("Enter your guess here: ")      
    try:    
        ANuser_input = [int(num) for num in ANuser_input.split()]      
    except ValueError:      
        print("Please enter numbers only!")    
        continue           
    if check_guess(ANuser_input, ANcorrect_sequence):         
        print("Well done!")  
        break
    else:  
        print("Try again! Press Enter to see the numbers again.")  
        input() 
        ANcorrect_sequence = start_game() 
