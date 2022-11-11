# BMI based on the BMI value.
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("Enter your height in meters: "));
weight = float(input("Enter your weight in kilograms: "));

bmi = weight / (height**2);

if(bmi > 35):
    print(f"Your BMI is {bmi:.2f}, you are clinically obese.");
elif(bmi > 30):
    print(f"Your BMI is {bmi:.2f}, you are obese.");
elif(bmi > 25):
    print(f"Your BMI is {bmi:.2f}, you are slightly overweight.");
elif(bmi > 18.5):
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.");
else:
    print(f"Your BMI is {bmi:.2f}, you are underweight");


