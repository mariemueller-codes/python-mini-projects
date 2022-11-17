# Make a rock, paper, scissors game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
choice = ['rock', 'paper', 'scissors']
# guess = input("Choose rock, paper or scissors: ").lower()
computer_choice = random.choices(choice)
print(computer_choice)
