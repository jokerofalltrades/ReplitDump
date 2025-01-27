import random
listOfNums = []
while len(listOfNums) < 8:
    num = random.randint(1,100)
    if num not in listOfNums: listOfNums.append(num)
global highscope
highscope = 0
def splitList(list, scope):
    global highscope
    scope += 1
    newList = list
    if highscope < scope: highscope = scope
    if len(list)//2 >= 1:
        newList = [list[:len(list)//2],list[len(list)//2:]]
        newList = [splitList(newList[0],scope),splitList(newList[1],scope)]
    return newList
def mergeSort(list, scope):
    scope -= 1

print(splitList(listOfNums, 0))
print(highscope)