import random
bot_number = random.randint(1,100)

print("Welcome to sigma guesser! You will try to guess the same number as Master Sigma! \n")

try:  
    number = int(input("Please input a number between 1 and 100: \n"))
    if number == 123456789:
        print(bot_number)
    else:
        bot_number = bot_number
except ValueError:  
    print("That's not a valid number! Please try again.")  
if number == bot_number:
    print("CORRECT! \n")
else:
    print("Try again!")
    while number != bot_number:
        
        try:  
            number = int(input("Please input a number between 1 and 100: \n"))  
        except ValueError:  
            print("That's not a valid number! Please try again.")
        if number == bot_number:  
            print("CORRECT!")  
            break  
        else:  
            print("Try again!")  
