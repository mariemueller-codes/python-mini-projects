
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

pizza_price = 0
pepperoni_price = 0
cheese_price = 0
total_bill = 0

if size == "S":
    pizza_price = 15
    if add_pepperoni == "Y":
        pepperoni_price = 2
    else:
        pepperoni_price = 0
elif size == "M":
    pizza_price = 20
    if add_pepperoni == "Y":
        pepperoni_price = 3
    else:
        pepperoni_price = 0
else:
    pizza_price = 25
    if add_pepperoni == "Y":
        pepperoni_price = 3
    else:
        pepperoni_price = 0

if extra_cheese == "Y":
    cheese_price = 1
else:
    cheese_price = 0

total_bill = pizza_price + pepperoni_price + cheese_price

print(f"Your final bill is: ${total_bill}.")