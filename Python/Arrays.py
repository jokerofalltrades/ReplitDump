fruits = ["apples","bananas","pears"]
fruits.append("pomegranate")
print(fruits[2])
GCSE = ["English Lit", "English Lang", "Maths", "Chemistry", "Physics", "Biology"]
finished = False
while not finished:
    more = input("Do you need to add an optional subject (Y or N) ")
    if more.upper() == "Y":
        GCSE.append(input("What optional subject do you take? "))
    else:
        finished = True
print(len(GCSE))

comSciMarks = [10,8,2,9,4,7]
for index in range(3):
    print(comSciMarks[index])
hiMark = None
lowMark = None
total = 0
for mark in comSciMarks:
    if hiMark == None: hiMark, lowMark = mark, mark
    print(mark)
    if mark>hiMark: hiMark = mark
    elif mark<lowMark: lowMark = mark
    total += mark
print(hiMark)
print(lowMark)
print(total/len(comSciMarks))
print(total)
