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

high = len(listOfNums)
low = 1
mid = high // 2
comparisons = 0
while numToFind != listOfNums[mid]:
    mid = (high + low) // 2
    if numToFind not in listOfNums:
        print(f"{numToFind} is not found in the list.")
        break
    elif numToFind > listOfNums[mid]:
        low = mid + 1
    elif numToFind < listOfNums[mid]:
        high = mid - 1
    else:
        print(f"{numToFind} is found at index {mid} after {comparisons} comparisons.")
    comparisons += 1
