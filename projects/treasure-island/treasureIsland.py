import image

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

print("You're at the crossroads. Where do you want to go? ")
choice = input('Type "left" or "right" ')

if (choice == "left"):
    print("You've come to a lake. There is an island in the middle of the lake.")
    choice2 = input('Type "wait" to wait for a boat. Type "swim" to swim across.')
    if(choice2 == "wait"):
        print("You arrived at the island unharmed.")
        print("There is a house with 3 doors. One red, one yellow and one blue.")
        door_color = input("Which color do you choose? ")
        if(door_color == "yellow"):
            print("You win!")
        elif(door_color == "red"):
            print("Burned by fire. Game Over.")
        elif(door_color == "blue"):
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over")
    else:
        ("You get attacked by an angry trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")