# Anthony Memory

import time
import os
import random
memory_1 = random.randint(1,6)
memory_2 = random.randint(1,6)
memory_3 = random.randint(1,6)
memory_4 = random.randint(1,6)
memory_5 = random.randint(1,6)
memory_6 = random.randint(1,6)
memories = [memory_1, memory_2, memory_3, memory_4, memory_5, memory_6]
while len(memories) == len(set(memories)):
    memory_1 = random.randint(1,6)
    memory_2 = random.randint(1,6)
    memory_3 = random.randint(1,6)
    memory_4 = random.randint(1,6)
    memory_5 = random.randint(1,6)
    memory_6 = random.randint(1,6)

frames = [
    """  
    [ x ] [ x ] [ x ] [ x ]  
    [ x ] [ x ] [ x ] [ x ]  
    [ x ] [ x ] [ x ] [ x ]
    """,

    f"""
    [ {memory_1} ] [ {memory_5} ] [ {memory_2} ] [ {memory_3} ]  
    [ {memory_2} ] [ {memory_6} ] [ {memory_1} ] [ {memory_4} ]  
    [ {memory_3} ] [ {memory_4} ] [ {memory_6} ] [ {memory_5} ]  
    """,

    """  
    [ x ] [ x ] [ x ] [ x ]  
    [ x ] [ x ] [ x ] [ x ]  
    [ x ] [ x ] [ x ] [ x ]
    """,
]  
print("This is a memory game where you will try to remember what hidden cards match, and which ones dont. When you believe you have gotten the correct answer, type the numbers starting at the top left, and moving right as if reading a book. ")
while input("Type yes to start the game, or type your answer: ") == "yes" or input != (memory_1, memory_5, memory_2, memory_3, memory_2, memory_6, memory_1, memory_4, memory_3, memory_4, memory_6, memory_5) or input != "skibidi sigma":
    for frame in frames:
        os.system("cls" if os.name == "nt" else "clear")  # Clears screen for smooth animation
        print(frame)
        time.sleep(1)  # Adjust speed if needed
