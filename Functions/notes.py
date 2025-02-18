#Anthony Petersen, Functions notes
#Functions hold actions to be reused
numone = int(input("Please enter a number: \n"))
numtwo = int(input("Please enter another number: \n"))
def add(numone, numtwo):
    print(numone**numtwo)
    return numone+numtwo
add(numone,numtwo)
def values(type):
    return input(f"Please enter a {type}: \n")
name = values("name").strip().capitalize()
place = values("place").strip().capitalize()
verb = values("past tense verb").strip().lower()
print(f"{name} was really hungry well going to {place} because they {verb} the whole way there")