import random
import time
import math

money = 100
answerGiven = 0
flips = 0
oldManEncounters = 0
oldManPower = 0
winInARow = 0
_5FlipDialogue = 0
_5FlipDialogue2 = 0
_10FlipDialogue = 0
_10FlipDialogue2 = 0
taxDialogue = 0
trinkets = ["","","","","","","","","",""]
trinketSave = ""

def saveCodeGenerator():
    for item in trinkets:
        trinketSave += item
    newSaveCode = f"ValidSave:Money:{money}Flips:{flips}OldMan:{oldManEncounters}OldManPow:{oldManPower}WinRow:{winInARow}Trinkets:{trinketSave}".encode("utf-8").hex()
    return newSaveCode

def restructureTrinkets(savedTrinkets):
    for i in range(len(savedTrinkets)):
        trinkets += savedTrinkets[i]
    
def pause():
    time.sleep(0.2)


print("The Flipper: Welcome to the world's best casino: We have one enthralling game here.")
pause()
print("The Flipper: Our game is gambling on a coin flip. You start with 100 flipcoin.")
pause()
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
            oldManEncounters = int(saveCode[(saveCode.find("OldMan:")+7):saveCode.find("OldManPow:")])
            oldManPower = int(saveCode[(saveCode.find("OldManPow:")+10):saveCode.find("WinRow:")])
            winInARow = int(saveCode[(saveCode.find("WinRow:")+7):saveCode.find("Trinkets:")])
            trinketSave = str(saveCode[(saveCode.find("Trinkets:")+9):len(saveCode)])
            answerGiven = 1
            if math.log2(money) > flips:
                print("Mysterious Man: That is an illegal code.")
                answerGiven = 0
            restructureTrinkets(trinketSave)
        elif saveCode == "":
            print("Mysterious Man: Continue on with my companion.")
            answerGiven = 1          
        else:
            print("Mysterious Man: That is an invalid save code.")
print("The Flipper: Welcome to the Casino! Let's gamble on a coin toss!")
pause()
while money > 0:
    stake = 0
    bet = ""
    print(f"The Flipper: You currently have {money} flipcoin.")
    pause()
    print("The Flipper: Do you want to bet on heads, tails, or landing on its edge?")
    bet = input("The Flipper: Odds: Heads - x1.9 your stake, Tails - x1.9 your stake, Edge - x500 your stake (Enter Heads, Tails or Edge)")
    pause()
    while 1 > 0:
        stake = int(input("How much do you want to bet? "))
        if stake <= money and stake >= 0: break
        pause()
        print("That is an invalid stake.")
    bet = bet.lower()
    money -= stake
    flips += 1
    coinFlipDecider = random.randint(1,10000)
    if oldManPower > 0: coinFlipDecider = 1
    if coinFlipDecider <= 4999: result = "heads"
    if coinFlipDecider >= 5002: result = "tails"
    if coinFlipDecider >= 5000 and coinFlipDecider <= 5001: result = "edge"
    if result == bet:
        if bet != "edge":
            winamount = round(stake*1.9)
            money += winamount
        else:
            winamount = round(stake*500)
            money += winamount
            print("The Flipper: Impressive. You won while betting on edge. Very brave of you.")
            pause()
        if winInARow > 0:
            winInARow += 1
        else:
            winInARow = 1
        print(f"The Flipper: Wow! You won {winamount} flipcoin! Care to play again?")
        pause()
        response = input("The Flipper: Press 1 to play again, 2 to get your save code and 3 to leave.")
    else:
        if winInARow < 0 and bet != "edge":
            winInARow -= 1
        else:
            winInARow = -1
        print(f"Oh dear... It was {result}, you lost. Care to play again?")
        pause()
        response = input("The Flipper: Press 1 to play again, 2 to get your save code and 3 to leave.")
        pause()
    if response == "3":
        response = input("The Flipper: Are you sure you want to leave? Press 1 to continue, 2 to get your save code and leave and 3 to just leave.")
        if response == "2":
            print(f"Mysterious Man: {saveCodeGenerator()}")
            break
        elif response == "3":
            break
    if response == "2":
        print(f"Mysterious Man: {saveCodeGenerator()}")
    pause()
    if oldManPower > 0: oldManPower -= 1
    if random.randint(1,50) == 50:
        if oldManEncounters == 0:
            print("???: Psst... Hey Kid!")
            pause()
            print("Wise Old Man: Kid, don't bet on edge, the odds are 1 in 5000!")
            pause()
            print("Wise Old Man: These yung'uns could really use some help...")
            oldManEncounters += 1
        elif oldManEncounters == 1:
            print("Wise Old Man: Bet heads next time.")
            pause()
            print("Wise Old Man: I promise you will win.")
            pause()
            print("Wise Old Man: Give it everything you have.")
            oldManPower = 1
            oldManEncounters += 1
        elif oldManEncounters == 2:
            print("Wise Old Man: The Flipper is trying to 73696C656E6365 me.")
            pause()
            print("Wise Old Man: I don't have long before I'm 676F6E650A.")
            pause()
            print("Wise Old Man: Good Luck and bet on 6865616473 for the next 7468726565 goes.")
            oldManEncounters += 1
            oldManPower = 3
        elif oldManEncounters == 3:
            print("Old Man: Kid, I don't have lon-")
            pause()
            print("The Flipper: Enough of this.")
            pause()
            print("The Flipper: This knife'll do the trick...")
            pause()
            print("*A curtain is drawn and st*bbing sounds are heard. When the curtain is pulled, the old man is nowhere to be seen.*")
            pause()
            print("The Flipper: Good. Shall we continue?")
            oldManEncounters += 1
    if winInARow == 5 and _5FlipDialogue == 0:
        print("The Flipper: Someone's lucky today.")
        _5FlipDialogue = 1
    if winInARow == -5 and _5FlipDialogue2 == 0:
        print("The Flipper: Someone's unlucky today.")
        _5FlipDialogue2 = 1
    if winInARow == 10 and _10FlipDialogue == 0:
        print("The Flipper: Someone's extremely lucky toady.")
        _10FlipDialogue = 1
    if winInARow == -10 and _10FlipDialogue2 == 0:
        print("The Flipper: Someone's extremely unlucky today.")
        pause()
        print(f"The Flipper: Here. A gift. 10% of your flipcoins.")
        pause()
        result = int(money * 0.1) != 1 and "flipcoins" or "flipcoin"
        print(f"The Flipper: Enjoy your {int(money*0.1)} {result}.")
        money = int(money*1.1)
    if money >= 1000 and _10FlipDialogue2 == 1 and taxDialogue == 0:
        print("The Flipper: Remember when I gave you some flipcoins?")
        pause()
        print("The Flipper: I'll need some back. 10% to be exact.")
        money = round(money*0.9)
        taxDialogue = 1
    if flips == 20 and "1" not in trinkets:
        print("The Flipper: Here. A trinket of thanks.")
        pause()
        print("The Flipper: Enjoy my spider eye.")
        pause()
        print("The Flipper: Keep it safe.")
        trinkets[0] = "1"
    if flips == 50 and "2" not in trinkets:
        print("The Flipper: Huh. You seem to really like playing.")
        pause()
        print("The Flipper: Well... seen as you're still here...")
        pause()
        print("The Flipper: Have this 'Keep on Flipping' poster.")
        trinkets[1] = "2"
    if flips == 100 and "3" not in trinkets:
        print("The Flipper: You seem to like hanging around here.")
        pause()
        print("The Flipper: A puzzle, to pass the time...")
        pause()
        print("The Flipper: You can have a Rubik's Cube keychain.")
        trinkets[2] = "3"
    if flips == 250 and "4" not in trinkets:
        
        trinkets[3] = "4"
    if flips >= 500 and oldManEncounters == 4 and "6" not in trinkets:
        print("The Flipper: You seem to really miss that old man...")
        pause()
        print("The Flipper: Here. A memory of him. His skeleton.")
        pause()
        print("The Flipper: He would have wanted you to have had it anyway.")
        trinkets[5] = "6"
    #Add more dialogue
    pause()
        
if money > 0:
    print("The Flipper: Thanks for playing! See you again soon!")
else: 
    print("The Flipper: What a disappointing end...")
    pause()
    print("The Flipper: Thanks for your money.")
