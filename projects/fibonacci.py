# User input
response = int(input("Enter number: "))

# default value
a = 0
b = 1
c = 0
count = 1

print("Fibonacci Series: ", end=" ")

while (count <= response):
    print(b, end=" ")
    count += 1
    sum = a + b
    a = b
    b = sum

# work in progress
