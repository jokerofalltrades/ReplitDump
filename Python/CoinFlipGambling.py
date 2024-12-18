"""This module runs a coin gambling game. It is self contained."""

import random
import time
import math

# Remember to periodically check code with 'pycodestyle --first CoinFlipGambling.py' and 'pylint CoinFlipGambling.py'


def saveCodeGenerator(money, trinketSave, trinkets, flips, oldManEncounters, oldManPower, winInARow, rubikssolved):
    """Produces a save code, after compressing the user's trinkets."""
    for item in trinkets:
        trinketSave += str(item)
    newSaveCode = f"ValidSave:Money:{money}Flips:{flips}OldMan:{oldManEncounters}OldManPow:{oldManPower}WinRow:{winInARow}Trinkets:{trinketSave}CubeSolve:{rubikssolved}".encode("utf-8").hex()
    return newSaveCode


def restructureTrinkets(savedTrinkets, trinkets):
    """Recovers the player's trinkets after loading from a save."""
    for i in range(len(savedTrinkets)):
        trinkets += savedTrinkets[i]


def pause(timemodifier=1):
    """Generic time.sleep shortcut"""
    time.sleep(0.25*timemodifier)


def viewTrinkets(trinkets, flips, rubikssolved, money):
    """Displays information about the player's trinkets."""
    items = []
    rubiksdialogue = 0
    if "1" in trinkets: items.append("Spider's Eye")
    else: items.append("???")
    if "2" in trinkets: items.append("'Keep on Flipping' Poster")
    else: items.append("???")
    if "3" in trinkets: items.append("Rubik's Cube Keychain")
    else: items.append("???")
    if "4" in trinkets and flips <= 300: items.append("Half-Eaten Waffle")
    elif "4" in trinkets and flips > 300: items.append("Moldy Half-Eaten Waffle")
    else: items.append("???")
    if "5" in trinkets: items.append("placeholder")
    else: items.append("???")
    if "6" in trinkets: items.append("Old Man's Skeleton")
    else: items.append("???")
    if "7" in trinkets: items.append("placeholder")
    else: items.append("???")
    if "8" in trinkets: items.append("placeholder")
    else: items.append("???")
    if "9" in trinkets: items.append("placeholder")
    else: items.append("???")
    if "10" in trinkets: items.append("placeholder")
    else: items.append("???")
    print("The Flipper: Not this troublesome pack again...")
    pause()
    while True:
        print("Packsy: Hey there traveller!")
        pause()
        print("Packsy: You wish to know more about your trinkets... Sure!")
        pause(8)
        print(f"Packsy: Here are your trinkets:\n1: {items[0]}\n2: {items[1]}\n3: {items[2]}\n4: {items[3]}\n5: {items[4]}\n6: {items[5]}\n7: {items[6]}\n8: {items[7]}\n9: {items[8]}\n10: {items[9]}")
        pause(2)
        response = input("Packsy: Would you like to view additional information about one of these? If so type their number, else press enter. ")
        tempresponse = "0"
        if response == "":
            return money
        if response == "1" and items[0] != "???":
            print("Packsy: So, you wish to know more about the spider's eye?")
            pause()
            print("Packsy: Let me read you an exercpt from its description...")
            pause()
            print("Packsy: 'The spider eye is an eye from a spider. It gleams and glistens with a deep red colour in the light. Utterly Disgusting.'")
            pause(12)
            tempresponse = input("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ")
        elif response == "2" and items[1] != "???":
            print("Packsy: So, you wish to find out about the Poster?")
            pause()
            print("Packsy: Let me read you an exercpt from its description...")
            pause()
            print("Packsy: 'This poster inspires any and all gamblers to Keep on Flipping.'")
            pause(12)
            tempresponse = input("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ")
        elif response == "3" and items[2] != "???":
            print("Packsy: So, you wish to find out about the Rubik's Cube Keychain?")
            pause()
            print("Packsy: Let me read you an exercpt from its description...")
            pause()
            print("Packsy: 'Puzzling, isn't it. This cube has stumped many countless minds for decades. The one who solves it must be a nerd.'")
            pause(12)
            if rubiksdialogue == 0:
                rubiksdialogue = 1
                print("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ")
                pause(2)
                print("Packsy: Wait? Another Dialogue Option!")
                pause(8)
            tempresponse = input("Packsy: Press enter to continue playing, or type 1 to find out about another trinket, or # for a mystery dialogue option! ")
        elif response == "4" and items[3] != "???":
            print(f"Packsy: So, you wish to find out about the {items[3]}?")
            pause()
            print("Packsy: Let me read you an exercpt from its description...")
            pause()
            if items[3] == "Half-Eaten Waffle":
                print("Packsy: 'A half-eaten, unappetising waffle. You wonder who would be so stupid as to not finish their waffle. Might go moldy soon.'")
            else:
                print("Packsy: 'Euhhh... That stinks. 'A half-eaten, moldy waffle. It stinks really badly...' Euhhh, my eyes are watering.'")
            pause(12)
            tempresponse = input("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ")
        if tempresponse == "0":
            print("Packsy: You don't have that trinket, silly!")
            pause()
            tempresponse = input("Packsy: Press enter to continue playing, or type 1 to find out about another trinket. ")
        if tempresponse == "":
            return money
        if tempresponse == "#":
            if rubikssolved == 0:
                rubikssolved = 1
                print("Packsy: You want to solve it? Here!")
                pause(12)
                print("Packsy: Oh n- Wai- What? You solved it?")
                pause()
                print("Packsy: Here, have 50 flipcoin!")
                money += 50
                tempresponse = input("Packsy: Press enter to continue playing, or type 1 to find out about another trinket. ")
            else:
                print("Packsy: You already solved the cube, silly!")
                tempresponse = input("Packsy: Press enter to continue playing, or type 1 to find out about another trinket. ")
        if tempresponse == "":
            return money


def main():
    """Runs the main game loop"""
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
    trinkets = ["", "", "", "", "", "", "", "", "", ""]
    trinketSave = ""
    killScene = 0
    rubikssolved = 0
    result = ""
    print("The Flipper: Welcome to the world's best casino: We have one enthralling game here.")
    pause()
    print("The Flipper: Our game is gambling on a coin flip. You start with 100 flipcoin.")
    pause()
    hereBefore = input("The Flipper: If you have wasted your time here before, enter 1, else enter 2. ")
    # savecode code
    if hereBefore == "1":
        while answerGiven == 0:
            print("Mysterious Man: Welcome to my Save Cove.")
            hexSaveCode = input("Mysterious Man: If you do not have a save press enter. Else please enter your save code: ")
            bytesObj = bytes.fromhex(hexSaveCode)
            saveCode = bytesObj.decode('utf-8')
            if saveCode.find("ValidSave:") != -1:
                money = int(saveCode[(saveCode.find("Money:")+6):(saveCode.find("Flips:"))])
                flips = int(saveCode[(saveCode.find("Flips:")+6):saveCode.find("OldMan:")])
                oldManEncounters = int(saveCode[(saveCode.find("OldMan:")+7):saveCode.find("OldManPow:")])
                oldManPower = int(saveCode[(saveCode.find("OldManPow:")+10):saveCode.find("WinRow:")])
                winInARow = int(saveCode[(saveCode.find("WinRow:")+7):saveCode.find("Trinkets:")])
                trinketSave = str(saveCode[(saveCode.find("Trinkets:")+9):saveCode.find("CubeSolve:")])
                rubikssolved = int(saveCode[(saveCode.find("CubeSolve:")+10):len(saveCode)])
                answerGiven = 1
                if math.log2(money) - math.log2(100) > flips:
                    print("Mysterious Man: That is an illegal code.")
                    answerGiven = 0
                restructureTrinkets(trinketSave,trinkets)
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
        bet = input("The Flipper: Odds: Heads - x1.9 your stake, Tails - x1.9 your stake, Edge - x500 your stake (Enter Heads, Tails or Edge) ")
        pause()
        # check for valid stake
        while True:
            stake = input("How much do you want to bet? ")
            try:
                stake = int(stake)
            except ValueError:
                print("Please enter a valid input.")
                stake = 0
            else:
                stake = int(math.ceil(stake))
                if 0 < stake <= money: break
                pause()
                print("That is an invalid stake.")
            pause()
        bet = bet.lower()
        money -= stake
        flips += 1
        #decides coin flip
        coinFlipDecider = random.randint(1,10000)
        if oldManPower > 0: coinFlipDecider = 1
        if coinFlipDecider <= 4999: result = "heads"
        if coinFlipDecider >= 5002: result = "tails"
        if 5000 <= coinFlipDecider <= 5001: result = "edge"
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
            response = input("The Flipper: Press 1 to play again, 2 to get your save code, 3 to view your trinkets and 4 to leave. ")
        else:
            if winInARow < 0 and bet != "edge":
                winInARow -= 1
            else:
                winInARow = -1
            print(f"Oh dear... It was {result}, you lost. Care to play again?")
            pause()
            response = input("The Flipper: Press 1 to play again, 2 to get your save code, 3 to view your trinkets and 4 to leave. ")
            pause()
        if response == "4":
            response = input("The Flipper: Are you sure you want to leave? Press 1 to return to the game, 2 to get your save code and leave and 3 to just leave. ")
            if response == "2":
                print(f"Mysterious Man: {saveCodeGenerator(money, trinketSave, trinkets, flips, oldManEncounters, oldManPower, winInARow, rubikssolved)}")
                break
            if response == "3":
                killScene = 1
                break
        if response == "2":
            print(f"Mysterious Man: {saveCodeGenerator(money, trinketSave, trinkets, flips, oldManEncounters, oldManPower, winInARow, rubikssolved)}")
        if response == "3":
            money = viewTrinkets(trinkets, flips, rubikssolved, money)
        pause()
        #old man stuff
        if oldManPower > 0: oldManPower -= 1
        if random.randint(1,50) == 50:
            if oldManEncounters == 0:
                print("???: Psst... Hey Kid!")
                pause(4)
                print("Wise Old Man: Kid, don't bet on edge, the odds are 1 in 5000!")
                pause(4)
                print("Wise Old Man: These yung'uns could really use some help...")
                oldManEncounters += 1
            elif oldManEncounters == 1:
                print("Wise Old Man: Bet heads next time.")
                pause(4)
                print("Wise Old Man: I promise you will win.")
                pause(4)
                print("Wise Old Man: Give it everything you have.")
                oldManPower = 1
                oldManEncounters += 1
            elif oldManEncounters == 2:
                print("Wise Old Man: The Flipper is trying to 73696C656E6365 me.")
                pause(4)
                print("Wise Old Man: I don't have long before I'm 676F6E650A.")
                pause(4)
                print("Wise Old Man: Good Luck and bet on 6865616473 for the next 7468726565 goes.")
                oldManEncounters += 1
                oldManPower = 3
            elif oldManEncounters == 3:
                print("Old Man: Kid, I don't have lon-")
                pause(4)
                print("The Flipper: Enough of this.")
                pause(4)
                print("The Flipper: This knife'll do the trick...")
                pause(4)
                print("*A curtain is drawn and st*bbing sounds are heard. When the curtain is pulled, the old man is nowhere to be seen.*")
                pause(4)
                print("The Flipper: Good. Shall we continue?")
                oldManEncounters += 1
        #random dialogue bits
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
            print(f"The Flipper: Here. A gift. 10% of your flipcoin.")
            pause()
            print(f"The Flipper: Enjoy your {int(money*0.1)} flipcoin.")
            money = int(money*1.1)
        if money >= 1000 and _10FlipDialogue2 == 1 and taxDialogue == 0:
            print("The Flipper: Remember when I gave you some flipcoin?")
            pause()
            print("The Flipper: I'll need some back. 10% to be exact.")
            money = round(money*0.9)
            taxDialogue = 1
        #trinkets
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
            print("The Flipper: You really are dedicated to this...")
            pause()
            print("The Flipper: So I may as well award you.")
            pause()
            print("The Flipper: You can have my half-eaten waffle.")
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

    if killScene == 1 and money > 100:
        print("*As you begin to walk away you hear The Flipper bark orders at his servant.*")
        pause(4)
        print("Servant: Must I?")
        pause(4)
        print("*Suddenly you feel a sharp pain in the back of your head and you fall to the floor.*")
        pause(8)
        print("The Flipper: The house. Always. WINS.")
        pause(4)
        print("*As you feel yourself slipping away, The Flipper approaches and takes all your flipcoin, all the while with a manic smile.*")
    elif money > 0:
        print("The Flipper: Thanks for playing! See you again soon!")
    else:
        print("The Flipper: What a disappointing end...")
        pause()
        print("The Flipper: Thanks for your money.")

if __name__ == "__main__":
    main()
