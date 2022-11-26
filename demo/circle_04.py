# Write a Python program which accepts the radius of a circle from the user
# and compute the area.
from math import pi

radius = float(input("Enter radius of a circle: "))
area = pi * radius**2
print(f"The area of a circle with {radius} is {area:.2f}")
