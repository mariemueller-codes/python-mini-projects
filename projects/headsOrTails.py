# Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

import random

toss = random.randint(0,1)
if toss == 0:
    print("Heads")
else:
    print("Tails")
