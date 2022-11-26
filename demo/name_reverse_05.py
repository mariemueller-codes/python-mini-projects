import re
# name = input("Enter full name: ")
name = "Marie Mueller"
splitName = re.split('\W+', name)

x = 0
for i in splitName:
    x += 1
    print(splitName[len(splitName)-x])

# work in progress
