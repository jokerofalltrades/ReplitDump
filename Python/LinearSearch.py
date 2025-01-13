import random

listOfNums = []
while len(listOfNums) < 20:
    numToAdd = random.randint(1,100)
    if numToAdd not in listOfNums: listOfNums.append(numToAdd)
listOfNums.sort()

while True:
    try:
        numToFind = int(input("Enter a number between 1 and 100: "))
    except ValueError or TypeError:
        print("That is an invalid input.")
    else:
        if 0 < numToFind <= 100: break
        print("Please input a valid number.")

comparisons = 0
print(listOfNums)
for num in listOfNums:
    if num == numToFind:
        print(f"{numToFind} found at index {comparisons}, after {comparisons + 1} comparisons.")
        break
    comparisons += 1
if comparisons == len(listOfNums):
    print(f"{numToFind} is not in the list.")