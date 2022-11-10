# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = int(input("Enter your age: "));

age_left = 90 - age;
months_left = age_left * 12;
weeks_left = age_left * 52;
days_left = age_left * 365;

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.");