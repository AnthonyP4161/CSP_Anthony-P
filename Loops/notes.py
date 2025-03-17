#Anthony Petersen, Loops Notes
#What is a loop?
    #A repeating section of code
#What are the two types of loops?
    #for loop
nums = {12, 3, 66, 7, 3, 3, 2}
for num in nums:
    print(num)
    #while loop
x = 0
while x <10:
    print(x)
    x += 1
#What is iteration
    #An iteration is one instance of a loop
    #iteration is the amount of times you loop
#What are lists? 
    #A variable that stores multiple values
nums = [1,2,3,4,5,6,7,8,9,10]
names = ["Bob", "Jack", "Jim", "John", "Jamal"]
print(nums[3])
names[2] = "Jimmy"
names.pop(0)
names.insert(1, "Jeffrey")
names.insert(2, ["Jake", "Johnathon"])
print(names)
#How do you make lists in python? 
    #you make a variable and use brackets
    #Add items with correct data types
    #comma between each item
#How do you make for loops in python? 
for name in names:
    print(name)

for x in range(1,99,  1):
    print(x)
#How do you make while loops in python?
import random
goose = random.randint(1,20)
x = 1
while x < 20:
    if x == goose:
        print("goose")
        break
    else:
        print("duck")
    print("duck")
    x += 1
#continue restarts loop from start of while condition
#How do you make lists in C?
    #
#How do you make for loops in C?
    #
#How do you make while loops in C?
    #