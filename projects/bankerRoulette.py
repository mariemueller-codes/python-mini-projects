#  Write a program that will select a random name from a list of names

import random

demo_seed = int(input("Create a seed number: "))
random.seed(demo_seed)

name_string = input("Input a list of names, separated by a comma: ")
names = name_string.split(",")
name_list = []
name_list.extend(names)
random_name = name_list[random.randint(0, len(name_list)-1)]

print(f"{random_name} is in charge for today's standup.")
