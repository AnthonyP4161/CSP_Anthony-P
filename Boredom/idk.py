print("Hello, this is a quiz on random stuff. Be prepared, because you might get cooked! \n")
score = 0
question_1 =input("What meme is absolutely MASSIVE (P.S. Don't add too many letters because this meme may be DRAGGED out): \n").strip().lower()
if question_1 == "low taper fade":
    score = score+1
else:
    score = score
question_2 = input("What game that came out in 2020 popularized the term sus: \n").strip().lower()
if question_2 == "among us":
    score = score+1
else:
    score = score
question_3 = input("Who wears a mask with a smile, for hours at a time (P.S. They stare at a blank wall, well they hold back whats on their mind): \n").strip().lower()
if question_3 == "dream":
    score = score+1
else:
    score=score
question_4 = input("In what way, does Logan Paul like his cheese (P.S. just enter the adjective)").strip().lower()
if question_4 == "drippy":
    score = score+1
else:
    score = score
print("You got a score of", score, "out of 4")