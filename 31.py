#31 Write a for loop using an if statement, that appends each number to the 
# new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]

lst1=[111, 32, -9, -45, -17, 9, 85, -10]
newlst = []

for i in lst1:
    if i > 0:
        newlst.append(i)

print(f"The list having all positive number is {newlst}")