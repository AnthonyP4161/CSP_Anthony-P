# Anthony Petersen, Conditionals notes

name = input("What is your name:\n")

#What puts something inside of the “if” statement?

if name == "Anthony":
    print("Hi Anthony")
else:   # happens if condition is false
    print(f"hello {name}!")
#/\The tab at the front

#What do if statements do?

        # It checks if a conditoin is true and if it is it will do the thing
if name == "Anthony":    # <== condition
    print("Hi Anthony") # <==this is what it does iif true

#What are boolean statements? 
        # the part of the conditional that is eather true or false/the true or false statement

if name == "Anthony": # <== this is the boolean statement
    print("Hi anthony")
else:   
    print(f"hello {name}!")

#What do else statements do?

        #if the boolean is false then the else statement happens

#What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("how many cookies are there:\n"))
# computers read top to bottom, check least likely things first
if num == 0: # <++ if always starts the conditional
    print("then there are none.")
elif num == 1: # <++ anything between needs to be elif
    print("there is one")
elif num <4:
    print ("There is a couple")
elif num <10:
    print("There are a few")
else: # <== else always ends a conditional
    print("there are many")
#What do each of the different symbols mean in conditionals?
# < Less Than
# > Greater than
# <= less than or equal to
# >= Greater than or equal to
# == equal to
# === *does not exist in python
# ! Not

#What are the 3 logical operators?
if num <10 and num > 5: #And means both booleans must be true
    print("This is a single digit number")

elif num <10 or num > 5: #or means at least one of the booleans must be true
    print("This is a  single digit number")

elif not num <10: #not changes to check if false
    print("This is a not single digit number")

#What are logical operators for?
   # Allows the code to handle more difficult questions, increases complexity.

#What does a nested conditional statement do?
if num <10:
    if num == 8:
        print("This prints at 8")
    else:
        print("this number is less then 10")
else: 
    print("the number is bigger then 10")