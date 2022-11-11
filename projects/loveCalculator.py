# Program that tests the compatibility between two people

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1.lower() + name2.lower()

love_score = 0
love_score2 = 0
true_score = 0

true_score += combined_name.count('t')
true_score  += combined_name.count('r')
true_score  += combined_name.count('u')
true_score  += combined_name.count('e')
love_score2 += combined_name.count('l')
love_score2 += combined_name.count('o')
love_score2 += combined_name.count('v')
love_score2 += combined_name.count('e')

str_love_score = str(true_score) + str(love_score2)
love_score = int(str_love_score)

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")