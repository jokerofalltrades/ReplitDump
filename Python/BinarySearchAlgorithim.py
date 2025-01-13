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
low = 0
mid = high // 2
comparisons = 0
def binarySearch(high, low, mid, comparisons):
    numNotInList = 0
    mid = (high + low) // 2
    if numToFind not in listOfNums:
        numNotInList = 1
    elif numToFind > listOfNums[mid]:
        mid, comparisons = binarySearch(high, mid + 1, mid, comparisons)
    elif numToFind < listOfNums[mid]:
        mid, comparisons = binarySearch(mid - 1, low, mid, comparisons)
    return [mid, comparisons + 1] if numNotInList == 0 else [0, 0]
print(listOfNums)
mid, comparisons = binarySearch(high, low, mid, comparisons)
print(f"{numToFind} is found at index {mid} after {comparisons} comparisons." if mid != 0 else f"{numToFind} is not found in the list.")
