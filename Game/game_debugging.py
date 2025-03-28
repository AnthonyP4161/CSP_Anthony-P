# Text Based Adventure
import time
import sys
import threading
import os
import random




#Game Functions
input_code = 0

code1_int = random.randint(1,9)
code2_int = random.randint(1,9)
code3_int = random.randint(1,9)

code1 = str(code1_int)

code2 = str(code2_int)

code3 = str(code3_int)

code = code1 + code2 + code3
 
def play_music():        
    pygame.init()          
    pygame.mixer.init()        
    try:    
        pygame.mixer.music.load('computer-keyboard-typing-290582.mp3')            
        pygame.mixer.music.play(-1)  # Loop the music    
    except Exception as e:    
        print("Error loading music:", e)    
 
try:        
    import pygame
    os.system("cls" if os.name == "nt" else "clear")        
except ImportError:        
    response = input("Pygame is not installed. Would you like to set it up for a better experience? (yes/no): ")        
    if response.lower() == 'yes':    
        print("Installing Pygame...")    
        os.system('pip install pygame')    
        input("Press Enter after installing Pygame to continue...")      
   
# Ask if the user wants to play music  


#play_music_input = input("Would you like to play music while typing? (yes/no): ")  


#if play_music_input.lower() == 'yes':  


#    music_thread = threading.Thread(target=play_music)  
#      
#    music_thread.start()  
 
# Your text-typing code here        












# Tick Tack Toe - Jared Lewis
def tic_tac_toe():
    clear_terminal()

    # Dictionary that holds the board
    slot = {
        1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'
    }

    # Function that draws the board
    def draw_board():
        return (f"{slot[1]} | {slot[2]} | {slot[3]}\n"
                f"{slot[4]} | {slot[5]} | {slot[6]}\n"
                f"{slot[7]} | {slot[8]} | {slot[9]}")

    # Welcomes player and draws the board
    print("\n")
    print("Welcome to Tic-Tac-Toe!")
    print("You are X and the computer is O")
    print(draw_board())

    # Main game loop
    while True:
        # Player's turn
        while True:
            try:
                player = int(input("Enter a slot (1-9):\n"))
                if player < 1 or player > 9:
                    print("Invalid slot. Try again.")
                    continue
                if slot[player] == 'X' or slot[player] == 'O':
                    print("Slot already taken. Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Enter a number between 1 and 9.")
                continue
        slot[player] = 'X'

        # Check if user won
        if (slot[1] == slot[2] == slot[3] or slot[4] == slot[5] == slot[6] or slot[7] == slot[8] == slot[9] or
            slot[1] == slot[4] == slot[7] or slot[2] == slot[5] == slot[8] or slot[3] == slot[6] == slot[9] or
            slot[1] == slot[5] == slot[9] or slot[3] == slot[5] == slot[7]):
            if (slot[1] == slot[2] == slot[3] == 'X' or slot[4] == slot[5] == slot[6] == 'X' or
                slot[7] == slot[8] == slot[9] == 'X' or slot[1] == slot[4] == slot[7] == 'X' or
                slot[2] == slot[5] == slot[8] == 'X' or slot[3] == slot[6] == slot[9] == 'X' or
                slot[1] == slot[5] == slot[9] == 'X' or slot[3] == slot[5] == slot[7]):
                print("You win!\nThe third digit is", code3, "\n")
                print("Press Enter to return to the map")
                while True:
                    if input() == "":
                        clear_terminal()
                        game_selection()
                        return  # Exit the function after game_selection()
                    else:
                        break

        # Check for tie after player's turn
        if all(cell == 'X' or cell == 'O' for cell in slot.values()):
            print("It's a tie!")
            print("Press Enter to return to the map")
            while True:
                if input() == "":
                    clear_terminal()
                    game_selection()
                    return  # Exit the function after game_selection()
                else:
                    continue

        # Computer's turn
        while True:
            computer = random.randint(1, 9)
            if slot[computer] != 'X' and slot[computer] != 'O':
                slot[computer] = 'O'
                print(draw_board())

                # Check if computer won
                if (slot[1] == slot[2] == slot[3] == 'O' or slot[4] == slot[5] == slot[6] == 'O' or
                    slot[7] == slot[8] == slot[9] == 'O' or slot[1] == slot[4] == slot[7] == 'O' or
                    slot[2] == slot[5] == slot[8] == 'O' or slot[3] == slot[6] == slot[9] == 'O' or
                    slot[1] == slot[5] == slot[9] == 'O' or slot[3] == slot[5] == slot[7]):
                    print("You lost!\n")
                    print("Press Enter to return to the map")
                    while True:
                        if input() == "":
                            clear_terminal()
                            game_selection()
                            return  # Exit the function after game_selection()
                        else:
                            continue

                break

        # Check for tie after computer's turn
        if all(cell == 'X' or cell == 'O' for cell in slot.values()):
            print("It's a tie!")
            print("Press Enter to return to the map")
            while True:
                if input() == "":
                    clear_terminal()
                    game_selection()
                    return  # Exit the function after game_selection()
                else:
                    continue




#Alan De Lara
def hangman():
    clear_terminal()
    # word list  
    words = ["blood", "dark", "scared", "scream", "drenched", "helpless", "experiment", "choking", "crazed", "knife", "chainsaw", "gore", "corpse", "decomposed"]  
   
    def display_hangman(wrong_attempts):  
        if wrong_attempts == 0:  
            return """  
              ------  
              |      |  
              |        
              |        
              |        
              |        
            __|_________  
            """  
        elif wrong_attempts == 1:  
            return """  
              ------  
              |      |  
              |      O  
              |        
              |        
              |        
            __|_________  
            """  
        elif wrong_attempts == 2:  
            return """  
              ------  
              |      |  
              |      O  
              |      |  
              |        
              |        
            __|_________  
            """  
        elif wrong_attempts == 3:  
            return """  
              ------  
              |      |  
              |      O  
              |     /|
              |        
              |        
            __|_________
            """  
        elif wrong_attempts == 4:  
            return """  
              ------  
              |      |  
              |      O  
              |     /|\\
              |      |  
              |        
            __|_________
            """  
        elif wrong_attempts == 5:  
            return """  
              ------  
              |      |  
              |      O  
              |     /|\\
              |      |  
              |     / \\
            __|_________
            """  

        return [wrong_attempts]  
   
    def check_guess(letter, chosen_word, guessed_letters):  
        if letter in chosen_word:  
            guessed_letters.append(letter)  
            return True  
        else:  
            return False  
   
    # Main game loop  
    while True:  
        guessed_letters = []  # Reset guessed letters  
        wrong_attempts = 0    # Reset wrong attempts  
        max_attempts = 6      # max attempts  
        chosen_word = random.choice(words)  # Choose a new word  
   
        while wrong_attempts < max_attempts:  # Inner loop for guessing  
            print(display_hangman(wrong_attempts))  # Display hangman  
            display = ''.join(letter if letter in guessed_letters else '_' for letter in chosen_word)  
            print(display)  # Show the current state of the word  
   
            letter = input("Guess a letter: ")  
   
            if len(letter) == 1 and letter.isalpha():  # Validate input  
                if letter in guessed_letters:  
                    print("You've already guessed that letter.")  
                else:  
                    if check_guess(letter, chosen_word, guessed_letters):  
                        print("Good guess!")  
                    else:  
                        wrong_attempts += 1  
                        print("Wrong guess!")  
   
            if set(chosen_word).issubset(set(guessed_letters)):  # Win condition  
                print("Congratulations! You've guessed the word:", chosen_word)
                print("\n")
                print("The first digit is", code1, "\n")
                print("Press Enter to return to the map")
                while True:
                    if input() == "":
                        clear_terminal()
                        game_selection()
                        return  # Exit the function after returning to the map
                    else:
                        continue
           
        if wrong_attempts == max_attempts:  # Loss condition  
            print("Game over! The word was:", chosen_word)
            print("Press Enter to return to the map")
            while True:
                if input() == "":
                    clear_terminal()
                    game_selection()
                    return  # Exit the function after returning to the map
                else:
                    continue


#Anthony Petersen
def memory():
    clear_terminal()
    delay = 0.035

    ANinstructions = "This is a memory game that will flash the numbers and you have to repeat them.\n" \
                     "\n"\
                     "Press Enter to begin.\n"
    ANinstructions2 = "Please enter your answer, and remember to add spaces in between each number: \n"\
                     "HINT: If the flashed numbers where:\n"\
                     "[ 1 ] [ 4 ]\n"\
                     "[ 2 ] [ 5 ]\n"\
                     "[ 3 ] [ 6 ]\n"\
                     "You would enter the answer as '1 4 2 5 3 6'\n"

    def start_game():
        clear_terminal()
        # Generate random numbers for the memory sequence
        ANmemory_1 = random.randint(1, 9)
        ANmemory_2 = random.randint(1, 9)
        ANmemory_3 = random.randint(1, 9)
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

        # Display the frames
        for frame in ANframes:
            print(frame)
            time.sleep(2)  # Pause for a moment to show the frame
            os.system("cls" if os.name == "nt" else "clear")  # Clear the screen

        # Return the correct sequence
        return [ANmemory_2, ANmemory_3, ANmemory_3, ANmemory_1, ANmemory_1, ANmemory_2]

    def check_guess(ANuser_input, ANcorrect_guess):
        # Compare the user's input with the correct sequence
        if ANuser_input == ANcorrect_guess:
            print("Well done!")
            return True
        else:
            print("Try again!")
            return False
        
    # Display instructions
    for char in ANinstructions:
        print(char, end="")
        time.sleep(delay)
    input()  # Wait for the user to press Enter

    while True:  # Loop until the user guesses correctly
        ANcorrect_sequence = start_game()  # Display the frames and get the correct sequence
        ANuser_input = input(ANinstructions2).split()  # Get the user's input as a list of strings

        try:
            # Convert input to integers
            ANuser_input = [int(num) for num in ANuser_input]
            if check_guess(ANuser_input, ANcorrect_sequence):  # Check if the guess is correct
                print("\n")
                print("Digit #2 is", code2)
                print("Press Enter to return to the map")
                while True:
                    if input() == "":
                        clear_terminal()
                        game_selection()
                        return  # Exit the function after returning to the map
                    else:
                        continue
        except ValueError:
            print("Please enter numbers only!")  # Handle invalid input




# Where the story starts
# Fancy text functions - Douglas
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def flashing_text1(stop_event):
    sys.stdout.write("\033[?25l")  # Hide the cursor
    sys.stdout.flush()
    while not stop_event.is_set():
        sys.stdout.write("\rPress ENTER to continue   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r                                ")  # Ensure the line is cleared properly
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\033[?25h")  # Show the cursor again
    sys.stdout.flush()

def flashing_text2(stop_event):
    sys.stdout.write("\033[?25l")  # Hide the cursor
    sys.stdout.flush()
    while not stop_event.is_set():
        sys.stdout.write("\rPress ENTER to open door   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r                                ")  # Ensure the line is cleared properly
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\033[?25h")  # Show the cursor again
    sys.stdout.flush()

def flashing_text3(stop_event):
    sys.stdout.write("\033[?25l")  # Hide the cursor
    sys.stdout.flush()
    while not stop_event.is_set():
        sys.stdout.write("\rPress ENTER to restart at map.   ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write("\r                                ")  # Ensure the line is cleared properly
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\033[?25h")  # Show the cursor again
    sys.stdout.flush()


# sets the delay between each character printed
delay = 0.04


# Clear the terminal
clear_terminal()


# The Introduction - Jared
message1 = "Welcome user...\n"\
"The game you are about to play is a text based adventure game.\n"\
"This game will test your skills through a series of minigames.\n"\
"This game includes certain experiances that may cause anxiety or fear.\n"\
"This game is meant to possibly raise the heart rate\n"\
"and levels of adrenaline.\n"\
"Please be aware of this before you continue.\n"\
"\n"\
"May I welcome you to...\n"\
"\n"\
"THE UNDERWORLD\n"\
"created by:\n"\
"Alan De Lara\n"\
"Anthony Petersen\n"\
"Douglas London\n"\
"Jared Lewis\n"\
"\n"


# function to make text fancy - Douglas
for char in message1:
    print(char, end="", flush=True)
    time.sleep(delay)


stop_event = threading.Event()
thread = threading.Thread(target=flashing_text1, args=(stop_event,))
thread.start()


input()
stop_event.set()
thread.join()


clear_terminal()  # Clear the terminal again before the next message


# Itroduction to Backstory - Jared
message2 = "Chapter 1:\n"\
"A NORMAL CAR TRIP\n"\
"\n"\


# function to print the message slowly.
for char in message2:
    print(char, end="", flush=True)
    time.sleep(delay)


# Waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text1, args=(stop_event,))
thread.start()


input()
stop_event.set()
thread.join()
clear_terminal()


# Backstory - Jared
message3 = "You are a retired militry agent who served with the Navy Seals.\n"\
"It has been 5 years since your retirement and you currently live in a little nieghborhood in Colorado.\n"\
"So far, your life has seemed pretty normal.\n"\
"However, one day you were driving home from a car trip when everything darkened.\n"\
"You wake up in a dark room with no windows and no doors.\n"\
"The only thing you remember is a terrifying feeling of dread that you seemed to feel, just hours before.\n"\
"Suddenly you hear a distant\n"\
"\n"




# function to print the message slowly.
for char in message3:
    print(char, end="", flush=True)
    time.sleep(delay)


# dramatic end of Backstory
time.sleep(1)
print("Scream...\n")
time.sleep(1)




# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text1, args=(stop_event,))
thread.start()


input()
stop_event.set()
thread.join()
clear_terminal()


# Introduction to Chapter 2 - Jared
message4 = "Chapter 2:\n"\
"THE DARK ROOM\n"\
"\n"\


# function to print the message slowly.
for char in message4:
    print(char, end="", flush=True)
    time.sleep(delay)


# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text1, args=(stop_event,))
thread.start()


input()
stop_event.set()
thread.join()
clear_terminal()


# Chapter 2 - Jared
message5 = "As you feel around the room, you catch hold of a door handle.\n"\
"\n"


# function to print the message slowly.
for char in message5:
    print(char, end="", flush=True)
    time.sleep(delay)

# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text2, args=(stop_event,))
thread.start()

input()
stop_event.set()
thread.join()
clear_terminal()


message6 = "As the door slowly creaks open, you peer out into a long hallway.\n"\
"The hallway is dimly lit and has wallpaper that looks as though it is from an old orphanage.\n"\
"You walk down the hall and find a door with the words “TOO LATE” scribbled on it.\n"\
"\n"

# function to print the message slowly.
for char in message6:
    print(char, end="", flush=True)
    time.sleep(delay)

# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text2, args=(stop_event,))
thread.start()

input()
stop_event.set()
thread.join()
clear_terminal()

#Chapter 2
message7 = "The door scrapes loudly across the floor,\n"\
"and you find yourself in a small room.\n"\
"However, as you step inside, a metal sheet slides down in front of the door you just came from.\n"\
"Right next to the metal sheet, you notice a keypad.\n"\
"You try guessing the code on the keypad, but to no avail, you need a 3-digit code.\n"\
"You are trapped in the room!\n"\
"On the far wall, you see a map:\n"


# function to print the message slowly.
for char in message7:
    print(char, end="")
    time.sleep(delay)


# variable to store the map
map = " __________________________________\n"\
"|            Tic-Tac-Toe           |\n"\
"|               |   |              |\n"\
"|            ___|   |___           |\n"\
"|        ___| Map       |___       |\n"\
"| Hangman___             ___Memory |\n"\
"|           |___     ___|          |\n"\
"|            /  |___|              |\n"\
"|     Keypad    |   |              |\n"\
"|                Exit              |\n"\
"|__________________________________|\n"



# Function for keypad
def keypad():
    while True:
        print("Please enter the 3-digit code, or enter 'q' to return to the map.")
        input_code = input()
        if input_code == "q":
            clear_terminal()
            game_selection()  # Return to the map if the user enters 'q'
            return 
        elif input_code != code:
            print("Incorrect code. Try again.")
        elif input_code == code:
            clear_terminal()
            print("CORRECT!")
            time.sleep(1)
            clear_terminal()
            return 
        
#function for game selection
def game_selection():
    # prints the map
    print(map)

    # Game Selection
    message8 = "You are located where it says 'Map'.\n"\
    "Where do you choose to go?\n"\
    "HINT: The selections may have an answer to the code.\n"\
    "1. Tic-Tac-Toe\n"\
    "2. Hangman\n"\
    "3. Memory\n"\
    "4. Keypad\n"\
    "Enter the number you choose:\n"

    # function to print the message slowly.
    for char in message8:
        print(char, end="")
        time.sleep(delay)

    # Stupid Proofs input
    while True:
        try:
            user_input = int(input())
            if user_input in [1, 2, 3, 4]:
                break
            else:
                print("Invalid Input. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 4.")

    # Collects the user's input
    if user_input == 1:
        tic_tac_toe()
    elif user_input == 2:
        hangman()
    elif user_input == 3:
        memory()
    elif user_input == 4:
        clear_terminal()
        keypad()
       
# Calls The game_selection Funtion
game_selection()


# next message
print("CORRECT")
time.sleep(1)
clear_terminal()

message9 = "The metal sheet opens with a hiss, and you walk over to the door.\n"\
"On the door, in bold red letters, you read, “DO NOT ENTER.”\n"\
"Should you open the door?\n"\
"1 Yes\n"\
"2 No\n"\
"Enter the number you choose:\n"\


# function to print the message slowly.
for char in message9:
    print(char, end="")
    time.sleep(delay)


# Function for if input is 2
def message10():
    clear_terminal()
    message10 = "You leave the door closed and instead wander around the rooms looking for any way to escape,\n"\
    "but the only thing you find is a trap door with a heavy duty lock on it.\n"\
    "It appears the only way out is through the door.\n"\
    "Should you open the door?\n"\
    "1 Yes\n"\
    "Enter the number you choose:\n"


    # function to print the message slowly.
    for char in message10:
        print(char, end="")
        time.sleep(delay)
   
    # Collects the user's input
    while True:
            user_input = input()
            if user_input == "1":
                return True
            else:
                print("Your only way out is through the door. Please enter the number 1.")




# Collects and stupid proofs input
while True:
    user_input = input()
    if user_input == "1":
        break
    elif user_input == "2":
        if message10():
            break
    else:
        print("Invalid Input. Please enter 1 or 2.")
   


# next message
clear_terminal()
message11 = "You open the door, and spy a key on the floor just outside.\n"\
"You pick up the key and head back in to test it on the locked trapdoor.\n"\
"But Suddenly...\n"\


# function to print the message slowly.
for char in message11:
    print(char, end="")
    time.sleep(delay)


# next message
time.sleep(1)
message12 = "You hear a screeching coming from the end of the hall outside.\n"\
"The sound of multiple pairs of feet pattering down the hall stops you dead in your tracks.\n"\
"You lunge for the door and slam it just as you see a dark figure carreen towards you.\n"\
"Without a second thought your reflexes from years of Navy Seal training,\n"\
"cause you to slam the button on the keypad making the sheet of metal to slam down hard against the floor.\n"\
"You stand still for a few seconds, still processing what just happened.\n"\
"Your heart still pounding from the terrifying figure you only got a glimpse of.\n"\
"However, just a glimpse...\n"


# function to print the message slowly.
for char in message12:
    print(char, end="")
    time.sleep(delay)


# next message
time.sleep(1)
message13 = "was more than you wanted to see.\n"\
"\n"


# function to print the message slowly.
for char in message13:
    print(char, end="", flush=True)
    time.sleep(delay)


# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text1, args=(stop_event,))
thread.start()


input()
stop_event.set()
thread.join()
clear_terminal()


# Chapter 2 - Jared
def lock_picking():
    message14 = "Chapter 2:\n"\
    "THE BEAST\n"\
    "\n"


    # function to print the message slowly.
    for char in message14:
        print(char, end="", flush=True)
        time.sleep(delay)


    # waits for the user to press enter - Douglas
    stop_event = threading.Event()
    thread = threading.Thread(target=flashing_text1, args=(stop_event,))
    thread.start()


    input()
    stop_event.set()
    thread.join()
    clear_terminal()


    # next message - Jared
    message15 = "The pounding of the supernatural thing on the plate of metal interrupts your brief moment of silence.\n"\
    "You dash to the trapdoor in the center of the room,\n"\
    "and fumble with the key as you try to jam it into the old and tarnished lock.\n"\
    "With shaking hands you manage to twist the key, quickly sliding it off and fling open the hatch in the floor.\n"\
    "You jump down to the bottom of the stairs that are revealed, and sprint down the corridor.\n"\
    "To your dismay, you find another door, securely padlocked.\n"\
    "Frantically, you look around, and spy a few pins.\n"\
    "You have one chance of survival...\n"\
    "YOU HAVE TO PICK THE LOCK!\n"\


    # function to print the message slowly.
    for char in message15:
        print(char, end="")
        time.sleep(delay)


    # Lock Picking Game - Douglas
    time.sleep(3)
    clear_terminal()
    low = 1
    high = 6
    guess = 0
    num1 = random.randint(low, high)
    num2 = random.randint(low, high)
    num3 = random.randint(low, high)
    num4 = random.randint(low, high)

    correct_answer = [str(num1), str(num2), str(num3), str(num4)]
    correct_count = 0
    wrong_count = 0
    time_limit = 90  # Set the time limit in seconds
    time_up = False  # Flag to indicate if time is up

    # Timer function
    def timer():
        nonlocal time_up
        time.sleep(time_limit)
        time_up = True

    # Start the timer thread
    timer_thread = threading.Thread(target=timer)
    timer_thread.start()

    print("Correct Place: lists the amount of correct numbers in the correct placement.")
    print("Wrong Place: lists the amount of correst numbers in the wrong placement.")
    print("Find the correct numbers and their placement to pick the lock.")
    print("BUT YOU MUST HURRY!")
    print("Only "+str(time_limit)+" seconds until the Beast breaks in!\n")

    while guess == 0:
        if time_up:
            message27 = "The Beast breaks down the door and drags you off, you are never heard of again.\n"

            # function to print the message slowly.
            for char in message27:
                print(char, end="", flush=True)
                time.sleep(delay)

            # waits for the user to press enter
            stop_event = threading.Event()
            thread = threading.Thread(target=flashing_text3, args=(stop_event,))
            thread.start()

            input()
            stop_event.set()
            thread.join()
            clear_terminal()
            game_selection()

        if correct_count == 4:
            print("KA_KLUNK!")
            guess = 1
            time.sleep(2)
            return

        user_input = input("Enter your guess (4 digits between 1 and 6):\n")

        if len(user_input) != 4:
            print("Please enter exactly 4 characters.")
            continue

        correct_count = 0
        wrong_count = 0

        correct_positions = [False, False, False, False]
        wrong_positions = [False, False, False, False]
        temp_correct_answer = correct_answer.copy()

        for index in range(4):
            if user_input[index] == correct_answer[index]:
                correct_count += 1
                correct_positions[index] = True
                temp_correct_answer[index] = None
        for index in range(4):
            if not correct_positions[index]:
                for compare_index in range(4):
                    if not correct_positions[compare_index] and user_input[index] == str(temp_correct_answer[compare_index]) and temp_correct_answer[compare_index] is not None:
                        wrong_count += 1
                        temp_correct_answer[compare_index] = None

        print(f"Correct Place: {correct_count}, Wrong Place: {wrong_count}")

    # Stop the timer thread if the user succeeds
    time_up = True
    timer_thread.join()

    # Success message
    print("You successfully picked the lock!")
    print("Press Enter to continue.")
    input()
    clear_terminal()


    print(f"Correct: {correct_count}, Wrong: {wrong_count}")

    # Stop the timer thread if the user succeeds
    time_up = True
    timer_thread.join()

    # Success message
    print("You successfully picked the lock!")
    print("Press Enter to continue.")
    input()
    clear_terminal()


    print(f"Correct: {correct_count}, Wrong: {wrong_count}")
       
# Calls the lock picking game
lock_picking()


# next message
clear_terminal()
message16 = "You fling the door open, not caring for what might be on the other side.\n"\
"If anything, it is probably better than where you came from.\n"\
"You sprint down the new hallway and up a flight of stairs.\n"\
"All the cardio training from Navy Seals manages to help\n"\
"push your adrenalin fuelled body further and faster than ever,\n"\
"but it isn't fast enough...\n"


# function to print the message slowly.
for char in message16:
    print(char, end="")
    time.sleep(delay)


# brief pause for suspense
time.sleep(1)


# next message
message17 = "The creature is hot in pursuit, and you can practically feel it progressing towards you.\n"\
"Closing the distance faster than you would like.\n"\
"Then...\n"\


# function to print the message slowly.
for char in message17:
    print(char, end="")
    time.sleep(delay)


# brief pause for suspense
time.sleep(1)


# next message
message18 = "You see your chance.\n"\
"Just ahead, you see an opening to a large room, and further in the room,\n"\
"is a door with light peeking through the cracks.\n"\
"Not just any light, natural light.\n"\
"You pull any last ounce of strength from your weekend body and push it into your legs.\n"\
"Managing to propel your body the final distance.\n"\
"Never before has time passed so slowly.\n"\
"You can feel the pumping of each stride of your legs,\n"\
"the beat of your heart pumping furiously inside your chest,\n"\
"but worst of all, \n"\


# function to print the message slowly.
for char in message18:
    print(char, end="")
    time.sleep(delay)


# brief pause for suspense
time.sleep(1)


# next message
message19 = "the cold breath,\n"


# function to print the message slowly.
for char in message19:
    print(char, end="")
    time.sleep(delay)


# brief pause for suspense
time.sleep(1)


# next message
message20 = "the thumping legs,\n"


# function to print the message slowly.
for char in message20:
    print(char, end="")
    time.sleep(delay)


# brief pause for suspense
time.sleep(1)


# next message
message21 = "and the grazing touch of spidery fingers,\n"


# function to print the message slowly.
for char in message21:
    print(char, end="")
    time.sleep(delay)


# brief pause for suspense
time.sleep(1)


# next message
message22 = "of the beast, just inches behind you.\n"


# function to print the message slowly.
for char in message22:
    print(char, end="")
    time.sleep(delay)


# brief pause for suspense
time.sleep(3)


# next message
message23 = "You close the distance to the door in the fastest sprint of your life.\n"\
"Slamming into it, and immediately busting it open.\n"\
"As you find yourself outside, you turn to look back.\n"\
"Watching the creature skulk its way back to the heart of its layer, before you collapse onto\n"\
"the cold hard asphalt of an abandoned parking lot.\n"\


# function to print the message slowly.
for char in message23:
    print(char, end="", flush=True)
    time.sleep(delay)


# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text1, args=(stop_event,))
thread.start()


input()
stop_event.set()
thread.join()
clear_terminal()


message24 = "As you come to your senses, you realize the full moon shining, totally oblivious to the\n"\
"traumatizing experience you just endured.\n"\
"You scan your surroundings and spot your car, lying untouched in the parking lot.\n"\
"As you limp towards it, with every step igniting a fire in your legs, you notice a piece of paper\n"\
"pinned to your windshield by the wipers.\n"\
"On it reads the words, 'It was fun to play with you, I look forward to when we meet again.'\n"\
"You crumple the paper, then quickly slide into the front seat of your car, take the set of spare keys from under the\n"\
"car mat inside, and start the engine.\n"\
"You pull out of the parking lot and slam the gas pedal to the floor, putting as much distance\n"\
"between you and the building as possible.\n"\
"\n"


# function to print the message slowly.
for char in message24:
    print(char, end="",)
    time.sleep(delay)


# pause
time.sleep(1)


message25 = "THE END\n"


# function to print the message slowly.
for char in message25:
    print(char, end="",)
    time.sleep(delay)


# waits for the user to press enter - Douglas
stop_event = threading.Event()
thread = threading.Thread(target=flashing_text1, args=(stop_event,))
thread.start()

input()
stop_event.set()
thread.join()
clear_terminal()


# Credits
message26 = "Thank you for playing THE UNDERWORLD!\n"\
"If you didn't know, this game took over 1100 lines of code.\n"\
"If you could let us know that you appreciated our game, it would mean a lot.\n"\
"Once again, thank you, and fairwell.\n"\
"\n"\
"Credits:\n"\
"Tic-Tac-Toe  = Jared Lewis\n"\
"Hangman      = Alan De Lara\n"\
"Memory       = Anthony Petersen\n"\
"Lock Picking = Douglas London\n"\
"\n"\
"Story        = Jared Lewis\n"\
"Fancy Text   = Douglas London\n"\
"\n"\
"Debugging:\n"\
"Alan de Lara\n"\
"Anthony Petersen\n"

# function to print the message slowly.
for char in message26:
    print(char, end="",)
    time.sleep(delay)