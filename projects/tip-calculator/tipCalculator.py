# Program that calculates tip, total bill and splits it between number of parties

bill = float(input("Enter your bill: "))
tip = float(input("Enter tip percentage: "));
split = float(input("Enter number of people splitting the bill: "))

tip_percentage = (tip/100) 
total_bill = bill + (bill * tip_percentage)
split_bill = bill / split
print(f"Total bill is {total_bill:.2f} and each person has to pay {split_bill:.2f}")
