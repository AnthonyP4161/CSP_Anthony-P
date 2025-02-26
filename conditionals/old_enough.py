age = float(input("How many years old are you: \n"))
if(age >= 18):
    print("You can vote! \n")
elif(age >= 16):
    print("You can get a drivers license! \n")
elif(age == 15):
    print("You can get your learners permit! \n")
elif(age >= 4):
    print("You can go to school! \n")
else:
    print("You're a newborn, how are you even typing? \n")