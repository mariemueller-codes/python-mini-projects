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
choices = ['rock', 'paper', 'scissors']
guess = input("Choose rock, paper or scissors: ").lower()
computer_choice = choices[random.randint(0,2)]

def print_image(item):
    if item == 'rock':
        print(rock)
    elif item == 'paper':
        print(paper)
    elif item == 'scissors':
        print(scissors)

print(f"\nYou choose: {(guess)}")
print_image(guess)
print(f"\nComputer chooses: {(computer_choice)}")
print_image(computer_choice)

# game
if guess == computer_choice:
    print("It is a tie!")
elif guess == 'rock':
    if computer_choice == 'paper':
        print("You lose")
    else:
        print("You win")
elif guess == 'paper':
    if computer_choice == 'scissors':
        print("You lose")
    else:
        print("You win")
elif guess == 'scissors':
    if computer_choice == 'rock':
        print("You lose")
    else:
        print("You win")
else:
    print("Not a valid play")
