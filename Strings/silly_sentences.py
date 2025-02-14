#Anthony Petersen, Python Silly Sentences
name = input("Please enter a name: ").capitalize().strip()
place = input("Please enter the name of a city: ").capitalize().strip()
adjective = input("Please enter an adjective: ").lower().strip()
noun = input("Please enter a noun: ").lower().strip()
print(name, "went to", place, "to buy a", adjective, noun)