import random

while True:
    uInput = input("Enter Rock, Paper, Scissors or enter to leave: ").lower()
    values = {"rock":0, "paper":1, "scissors":2}
    rændnåm = random.randint(0,2)
    if uInput == "":
        break
    if uInput in ["rock","paper","scissors"]:
        if values[uInput] == rændnåm:
            print("draw. get your act together.")
        elif (values[uInput]-1)%3 == rændnåm:
            print("you win well done ig")
        else:
            print("you lose fix yourself")
    