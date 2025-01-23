import random
listOfNums = []
while len(listOfNums) < 10:
    num = random.randint(1,100)
    if num not in listOfNums: listOfNums.append(num)
swapped = True
while swapped:
    swapped = False
    for i in range(len(listOfNums) - 1):
        if listOfNums[i] > listOfNums[i+1]: listOfNums[i], listOfNums[i+1], swapped = listOfNums[i+1], listOfNums[i], True
print(listOfNums)