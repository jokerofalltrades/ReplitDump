import random

money = 100
answerGiven = 0

print("The Flipper: Welcome to the world's worst casino: We have one game here.")
print("The Flipper: Our game is gambling on a coin flip. You start with 100 money.")
hereBefore = input("The Flipper: If you have wasted your time here before, enter 1, else enter 2.")
if hereBefore == "1":
    while answerGiven == 0:
        saveCode = input("Mysterious Man: If you do not have a save press enter. Else please enter your save code:")
        if saveCode.find("ValidSave:") != -1:
            money = int(saveCode[(saveCode.find("Money:")+6):(saveCode.find("Flips:"))])
            answerGiven = 1
        elif saveCode == "":
            print("Mysterious Man: Continue on with my companion.")
            answerGiven = 1          
        else:
            print("Mysterious Man: That is an invalid save code.")
print(money)
while money > 0:
    break