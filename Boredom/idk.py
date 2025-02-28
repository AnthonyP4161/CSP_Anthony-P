print("Hello, this is a quiz on random stuff. Be prepared, because you might get cooked!")
print("Please note, all answers will consist of a single word answer, unless otherwise specified \n")
score = 0
answers = ("Here are the answers you got wrong \n")


question_1 =input("MULTI-WORD ANSWER \nWhat meme is absolutely MASSIVE: \n").strip().lower()
if question_1 == "low taper fade":
    score = score+1
else:
    answers += "You entered " + question_1 + ", when the correct answer was low taper fade.\n"


question_2 = input("MULTI-WORD ANSWER \nWhat game that came out in 2020 popularized the term sus: \n").strip().lower()
if question_2 == "among us":
    score = score+1
else:
    answers += "You entered " + question_2 + ", when the correct answer was among us.\n"


question_3 = input("Who wears a mask with a smile, for hours at a time (P.S. They stare at a blank wall, well they hold back whats on their mind): \n").strip().lower()
if question_3 == "dream":
    score = score+1
else:
    answers += "You entered " + question_3 + ", when the correct answer was dream.\n"


question_4 = input("In what way, does Logan Paul like his cheese (P.S. this is a single word answer) \n").strip().lower()
if question_4 == "drippy":
    score = score+1
else:
    answers += "You entered " + question_4 + ", when the correct answer was drippy.\n"


question_5 = input("A word used to describe the leader of a group, seen as above a beta male \n").strip().lower()
if question_5 == "alpha":
    score = score +1
else:
    answers += "You entered " + question_5 + ", when the correct answer was alpha.\n"


print("You got a score of", score, "out of 5 \n")


review = input("If you would like to see the correct answer, type yes, otherwise type no \n")
if review == "yes":
    print((answers))
else:
    print("Goodbye \n")