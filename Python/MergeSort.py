import random
listOfNums = []
while len(listOfNums) < 8:
    num = random.randint(1,100)
    if num not in listOfNums: listOfNums.append(num)

def mergeSort(list1, list2, n):
    width = 1
    while width < n:
        i = 0
        while i < n:
            list1, list2 = merge(list1, i, min(i+width, n), min(i+width*2, n), list2)
            i += 2*width
        width *= 2
        for i in range(n):
            list1[i] = list2[i]
    return list1

def merge(list1, iLeft, iRight, iEnd, list2):
    k,i,v = iLeft,iLeft,iRight
    while k < iEnd:
        if i < iRight and (v >= iEnd or list1[i] <= list1[v]):
            list2[k] = list1[i]
            i += 1
        else:
            list2[k] = list1[v]
            v += 1
        k += 1
    return list1, list2

print(mergeSort(listOfNums, [""]*len(listOfNums), len(listOfNums)))