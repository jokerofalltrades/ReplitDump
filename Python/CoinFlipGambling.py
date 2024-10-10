import random

money = 100
answerGiven = 0
flips = 0
oldManEncounters = 0

print("The Flipper: Welcome to the world's best casino: We have one enthralling game here.")
print("The Flipper: Our game is gambling on a coin flip. You start with 100 money.")
hereBefore = input("The Flipper: If you have wasted your time here before, enter 1, else enter 2.")
if hereBefore == "1":
    while answerGiven == 0:
        print("Mysterious Man: Welcome to my Save Cove.")
        hexSaveCode = input("Mysterious Man: If you do not have a save press enter. Else please enter your save code:")
        bytes_obj = bytes.fromhex(hexSaveCode)
        saveCode = bytes_obj.decode('utf-8')
        if saveCode.find("ValidSave:") != -1:
            money = int(saveCode[(saveCode.find("Money:")+6):(saveCode.find("Flips:"))])
            flips = int(saveCode[(saveCode.find("Flips:")+6):saveCode.find("OldMan:")])
            oldManEncounters = int(saveCode[(saveCode.find("OldMan:")+7):len(saveCode)])
            answerGiven = 1
        elif saveCode == "":
            print("Mysterious Man: Continue on with my companion.")
            answerGiven = 1          
        else:
            print("Mysterious Man: That is an invalid save code.")
print("The Flipper: Welcome to the Casino! Let's gamble on a coin toss!")
while money > 0:
    stake = 0
    bet = ""
    print(f"The Flipper: You currently have {money} money.")
    print("The Flipper: Do you want to bet on heads, tails, or landing on its edge.")
    bet = input("The Flipper: Odds: Heads - x1.9 your stake, Tails - x1.9 your stake, Edge - x500 your stake (Enter Heads, Tails or Edge)")
    while stake >= money or stake == 0:
        stake = int(input("How much do you want to bet?"))
    bet = bet.lower()
    money -= stake
    flips += 1
    coinFlipDecider = random.randint(1,10000)
    if coinFlipDecider <= 4999: result = "heads"
    if coinFlipDecider >= 5002: result = "tails"
    if coinFlipDecider >= 5000 and coinFlipDecider <= 5001: result = "edge"
    if result == bet:
        if bet != "edge":
            winamount = int(stake*1.9)
            money += winamount
        else:
            winamount = int(stake*500)
            money += winamount
        print(f"The Flipper: Wow! You won {winamount} money! Care to play again?")
        response = input("The Flipper: Press 1 to play again, 2 to get your save code and 3 to leave.")
    else:
        print(f"Oh dear... It was {result}, you lost. Care to play again?")
        response = input("The Flipper: Press 1 to play again, 2 to get your save code and 3 to leave.")
    if response == "3":
        response = input("The Flipper: Are you sure you want to leave? Press 1 to continue, 2 to get your save code and leave and 3 to just leave.")
        if response == "2":
            newSaveCode = f"ValidSave:Money:{money}Flips:{flips}OldMan:{oldManEncounters}".encode("utf-8").hex()
            print(f"Mysterious Man: {newSaveCode}")
            break
        elif response == "3":
            break
    if response == "2":
        newSaveCode = f"ValidSave:Money:{money}Flips:{flips}OldMan:{oldManEncounters}".encode("utf-8").hex()
        print(f"Mysterious Man: {newSaveCode}")
    if random.randint(1,100) == 100:
        if oldManEncounters == 0:
            print("???: Psst... Hey Kid!")
            print("Wise Old Man: Kid, don't bet on edge, the odds are 1 in 5000!")
            print("Wise Old Man: These yung'uns could really use some help...")
            oldManEncounters += 1

print("The Flipper: Thanks for playing! See you again soon!")