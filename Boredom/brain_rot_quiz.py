print(" \nHello, this is a quiz on random stuff. Be prepared, because you might get cooked!")
print(" \nPlease note, all answers will consist of a single word answer, unless otherwise specified \n")
score = 0
answers = ("Here are the answers you got wrong \n")


question_1 =input("MULTI-WORD ANSWER \nQuestion 1 \nWhat meme is absolutely MASSIVE: \n").strip().lower()
if question_1 == "low taper fade":
    score = score+1
else:
    answers += "You entered " + question_1 + ", when the correct answer was low taper fade.\n"


question_2 = input("MULTI-WORD ANSWER \nQuestion 2 \nWhat game that came out in 2020 popularized the term sus: \n").strip().lower()
if question_2 == "among us":
    score = score+1
else:
    answers += "You entered " + question_2 + ", when the correct answer was among us.\n"


question_3 = input("Question 3 \nWho wears a mask with a smile, for hours at a time (P.S. They stare at a blank wall, well they hold back whats on their mind): \n").strip().lower()
if question_3 == "dream":
    score = score+1
else:
    answers += "You entered " + question_3 + ", when the correct answer was dream.\n"


question_4 = input("Question 4 \nIn what way, does Logan Paul like his cheese (P.S. this is a single word answer) \n").strip().lower()
if question_4 == "drippy":
    score = score+1
else:
    answers += "You entered " + question_4 + ", when the correct answer was drippy.\n"


question_5 = input("Question 5 \nA word used to describe the leader of a group, often seen as better than a beta male \n").strip().lower()
if question_5 == "alpha":
    score = score +1
else:
    answers += "You entered " + question_5 + ", when the correct answer was alpha.\n"


question_6 = input("MULTI-WORD ANSWER \nQuestion 6 \nWhat popular icon among the generation known as Gen Alpha, is a head coming out of a toilet \n").strip().lower()
if question_6 == "skibidi toilet":
    score = score+1
else:
    answers += "You entered " + question_6 + ", when the correct answer was skibidi toilet. \n"


question_7 = input("Question 7 \nWhat was the name of the lunch food box created by Logan Paul, Mr. Beast, and KSI called \n").strip().lower()
if question_7 == "lunchly":
    score=score+1
else:
    answers += "You entered " + question_7 + ", when the correct answer was lunchly. \n"


question_8 = input("Question 8 \nA term associated with one's ability to attract someone, short for charisma \n")
if question_8 == "rizz":
    score = score+1
else:
    answers += "You entered " + question_8 + ", when the correct answer was rizz. \n"
    
print("You got a score of", score, "out of 8" "\n")

review = input("If you would like to see the correct answer, type yes, otherwise type no \n")
if review == "yes":
    if score == 8:
        print("You got everything right, so there's no wrong answers to show!")
    else:
        print((answers))
else:
    print("Goodbye \n")