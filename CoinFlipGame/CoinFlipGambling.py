"""This module runs a coin gambling game. It is self contained."""

import random
import time
import math
import os

# Remember to periodically check code with 'pycodestyle --first CoinFlipGambling.py' and 'pylint CoinFlipGambling.py'
# TODO:
# - Add more trinkets
# - Add the abillity to equip a trinket
# - Code in the moldy waffle stuff to water his eyes
# - Figure out what the 9th trinket is (the one that kills him)
# - Endings:
# Murder ending: Kill the Flipper
# Mercy Ending: About to kill Flipper but spare him
# Use for mercy ending: Thomas: Hello I'm so big right now im the grey (so big)
# Puppet ending: Refuse the Wise messenger's help and reach 1500 flips
# 'Own Knowledge' ending: Refuse Wise Messenger's help but still kill flipper
# 'YOU IDIOT' ending: Refuse Wise Messenger's help and reach mercy ending - flipper entraps you
#Game Over / House always wins
# - Add endings tracker, give special trinket 11 if you reach all canonical endings
# - Use Thomas as playtester
# - Possibly improve encryption of save code? (maybe post release update)
# - Keep a record of saves / savebank


def startUp() -> float:
    """Sets up the game."""
    textSpeed = inputAndClear("Settings Tinkerer: Before we start, how fast would like the text to appear? (V for Very Slow, S for Slow, M for Medium (Default) or F for Fast or X for Very Fast) ")
    global pauseSpeed
    while True:
        if textSpeed.lower() == "v":
            pauseSpeed = 1
            break
        if textSpeed.lower() == "s":
            pauseSpeed = 0.75
            break
        if textSpeed.lower() == "m":
            pauseSpeed = 0.5
            break
        if textSpeed.lower() == "f":
            pauseSpeed = 0.35
            break
        if textSpeed.lower() == "x":
            pauseSpeed = 0.25
            break
        textSpeed = input("Settings Tinkerer: Please enter a valid input. (V for Very Slow, S for Slow, M for Medium or F for Fast or X for Very Fast) ")
    printAndPause("Settings Tinkerer: Have fun with the game!")


def saveCodeGenerator(money, trinketSave, trinkets, flips, oldManEncounters, oldManPower, winInARow, rubikssolved, wiseMessengerEncounters) -> str:
    """Produces a save code, after compressing the user's trinkets."""
    trinketSave = "".join(str(item) for item in trinkets)
    newSaveCode = f"ValidSave:Money:{money}Flips:{flips}OldMan:{oldManEncounters}OldManPow:{oldManPower}WinRow:{winInARow}Trinkets:{trinketSave}CubeSolve:{rubikssolved}WiseMessenger:{wiseMessengerEncounters}Pause:{pauseSpeed}".encode("utf-8").hex()
    return newSaveCode


def printAndPause(tobePrinted, timemodifier=1):
    """Prints with a Generic time.sleep() shortcut - timemodifier is multiplied by 0.25 and inputted into a time.sleep() function."""
    print(tobePrinted)
    time.sleep(pauseSpeed*timemodifier)

def inputAndClear(toPrint) -> str:
    """Clears the input after it is entered."""
    userInput = input(toPrint)
    clear()
    return userInput

def clear():
    """Clears the screen."""
    os.system('cls' if os.name=='nt' else 'clear')

def viewTrinkets(trinkets, flips, rubikssolved, money) -> int:
    """Displays information about the player's trinkets."""
    rubiksdialogue = 0
    items = ["Spider's Eye" if "1" in trinkets else "???",
             "'Keep on Flipping' Poster" if "2" in trinkets else "???",
             "Rubik's Cube Keychain" if "3" in trinkets else "???",
             "Half-Eaten Waffle" if "4" in trinkets and flips <= 300 else
             "Moldy Half-Eaten Waffle" if "4" in trinkets and flips > 300 else "???",
             "Golden Spear" if "5" in trinkets else "???",
             "Old Man's Skeleton" if "6" in trinkets else "???",
             "placeholder" if "7" in trinkets else "???",
             "placeholder" if "8" in trinkets else "???",
             "placeholder" if "9" in trinkets else "???",
             "placeholder" if "10" in trinkets else "???"]
    printAndPause("The Flipper: Not this troublesome pack again...")
    while True:
        printAndPause("Packsy: Hey there traveller!")
        printAndPause("Packsy: You wish to know more about your trinkets... Sure!",8)
        printAndPause(f"Packsy: Here are your trinkets:\n1: {items[0]}\n2: {items[1]}\n3: {items[2]}\n4: {items[3]}\n5: {items[4]}\n6: {items[5]}\n7: {items[6]}\n8: {items[7]}\n9: {items[8]}\n10: {items[9]}",2)
        response = inputAndClear("Packsy: Would you like to view additional information about one of these? If so type their number, else press enter. ")
        tempresponse = "0"
        if response == "":
            return money
        if response == "1" and items[0] != "???":
            printAndPause("Packsy: So, you wish to know more about the spider's eye?")
            printAndPause("Packsy: Let me read you an exercpt from its description...")
            printAndPause("Packsy: 'The spider eye is an eye from a spider. It gleams and glistens with a deep red colour in the light. Utterly Disgusting.'",12)
            tempresponse = inputAndClear("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ")
        elif response == "2" and items[1] != "???":
            printAndPause("Packsy: So, you wish to find out about the Poster?")
            printAndPause("Packsy: Let me read you an exercpt from its description...")
            printAndPause("Packsy: 'This poster inspires any and all gamblers to Keep on Flipping.'",12)
            tempresponse = inputAndClear("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ")
        elif response == "3" and items[2] != "???":
            printAndPause("Packsy: So, you wish to find out about the Rubik's Cube Keychain?")
            printAndPause("Packsy: Let me read you an exercpt from its description...")
            printAndPause("Packsy: 'Puzzling, isn't it. This cube has stumped many countless minds for decades. The one who solves it must be a nerd.'",12)
            if rubiksdialogue == 0:
                rubiksdialogue = 1
                printAndPause("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ",4)
                printAndPause("Packsy: Wait? Another Dialogue Option!",6)
            tempresponse = inputAndClear("Packsy: Press enter to continue playing, or type 1 to find out about another trinket, or 2 for a mystery dialogue option! ")
        elif response == "4" and items[3] != "???":
            printAndPause(f"Packsy: So, you wish to find out about the {items[3]}?")
            printAndPause("Packsy: Let me read you an exercpt from its description...")
            if items[3] == "Half-Eaten Waffle":
                printAndPause("Packsy: 'A half-eaten, unappetising waffle. You wonder who would be so stupid as to not finish their waffle. Might go moldy soon.'")
            else:
                printAndPause("Packsy: Euhhh... That stinks. 'A half-eaten, moldy waffle. It stinks really badly...' Euhhh, my eyes are watering.",12)
            tempresponse = inputAndClear("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ")
        elif response == "5" and items[4] != "???":
            printAndPause("Packsy: So, you wish to find out about the Golden Spear?")
            printAndPause("Packsy: Let me read you an exercpt from its description...")
            printAndPause("Packsy: 'A Golden Spear, thousands of years old. Its handle and blade have been meticulously crafted to ensure a sharp edge.'",12)
            tempresponse = inputAndClear("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ")
        elif response == "6" and items[5] != "???":
            printAndPause("Packsy: So, you wish to find out about the Old Man's Skeleton?")
            printAndPause("Packsy: Poor guy...")
            printAndPause("Packsy: Did he really deser-")
            printAndPause("The Flipper: Keep your mouth shut. If you want to li- be my friend.",4)
            printAndPause("Packsy: ...")
            printAndPause("Packsy: Let me read you an exercpt from its description then...")
            printAndPause("Packsy: 'The Old Man's Skeleton. Comprised of 206 bones.'",8)
            printAndPause("Packsy: Hold up. I think I see something written on the skeleton.",8)
            tempresponse = inputAndClear("Packsy: Hmm... Press enter to continue playing, type 1 to find out about another trinket or type 2 to inspect the skeleton. ")
        elif response == "10" and items[9] != "???":
            printAndPause("Packsy: So, you wish to find out about the Four Leaf Clover?")
            printAndPause("Packsy: Let me read you an exercpt from its description...")
            printAndPause("Packsy: 'A Four Leaf Clover. Supposed to be a symbol of luck. It seems to have wilted slightly.'",12)
            tempresponse = inputAndClear("Packsy: Inspiring, isn't it! Press enter to continue playing, or type 1 to find out about another trinket. ")
        if tempresponse == "0":
            printAndPause("Packsy: You don't have that trinket, silly!")
            tempresponse = inputAndClear("Packsy: Press enter to continue playing, or type 1 to find out about another trinket. ")
        # For responses following a normal trinket
        if tempresponse == "":
            return money
        if tempresponse == "2" and response == "3":
            if rubikssolved == 0:
                rubikssolved = 1
                printAndPause("Packsy: You want to solve it? Here!",12)
                printAndPause("Packsy: Oh n- Wai- What? You solved it?")
                printAndPause("Packsy: Here, have 50 flipcoin!")
                money += 50
                tempresponse = inputAndClear("Packsy: Press enter to continue playing, or type 1 to find out about another trinket. ")
            else:
                printAndPause("Packsy: You already solved the cube, silly!")
                tempresponse = inputAndClear("Packsy: Press enter to continue playing, or type 1 to find out about another trinket. ")
        if tempresponse == "2" and response == "6":
            printAndPause("Packsy: Let's have a closer look shall we...",2)
            printAndPause("Packsy: *inaudible muttering*",6)
            printAndPause("Packsy: Oh! There! Look! It's a... poem?",2)
            printAndPause("Packsy: 'Mold makes watery eyes\nand spears do make HIM cry\nand just 2g of cyanide to make HIM die'",12)
            printAndPause("Packsy: Interesting... Ominous... I wonder who they're talking about when the say HIM...",8)
            tempresponse = inputAndClear("Packsy: Anyway, Press enter to continue playing, or type 1 to find out about another trinket. ")
        # For responses following special events
        if tempresponse == "":
            return money


def main():
    """Runs the main game loop"""
    global pauseSpeed
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
    trinkets = [" "]*10
    trinketSave = ""
    killScene = 0
    rubikssolved = 0
    result = ""
    wiseMessengerEncounters = 0
    pauseSpeed = 0.5
    printAndPause("The Flipper: Welcome to the world's best casino: We have one enthralling game here.")
    printAndPause("The Flipper: Our game is gambling on a coin flip. You start with 100 flipcoin.")
    hereBefore = inputAndClear("The Flipper: If you have wasted your time here before, enter 1, else enter 2. ")
    # savecode code
    if hereBefore == "1":
        while answerGiven == 0:
            print("Mysterious Man: Welcome to my Save Cove.")
            hexSaveCode = inputAndClear("Mysterious Man: If you do not have a save press enter. Else please enter your save code: ")
            bytesObj = bytes.fromhex(hexSaveCode)
            saveCode = bytesObj.decode('utf-8')
            if saveCode.find("ValidSave:") != -1:
                money = int(saveCode[(saveCode.find("Money:")+6):(saveCode.find("Flips:"))])
                flips = int(saveCode[(saveCode.find("Flips:")+6):saveCode.find("OldMan:")])
                oldManEncounters = int(saveCode[(saveCode.find("OldMan:")+7):saveCode.find("OldManPow:")])
                oldManPower = int(saveCode[(saveCode.find("OldManPow:")+10):saveCode.find("WinRow:")])
                winInARow = int(saveCode[(saveCode.find("WinRow:")+7):saveCode.find("Trinkets:")])
                trinkets = list(str(saveCode[(saveCode.find("Trinkets:")+9):saveCode.find("CubeSolve:")]))
                rubikssolved = int(saveCode[(saveCode.find("CubeSolve:")+10):saveCode.find("WiseMessenger:")])
                wiseMessengerEncounters = round(float(saveCode[(saveCode.find("WiseMessenger:")+14):saveCode.find("Pause:")]),1)
                pauseSpeed = float(saveCode[(saveCode.find("Pause:")+6):])
                answerGiven = 1
                if math.log2(money) - math.log2(100) > flips:
                    printAndPause("Mysterious Man: That is an illegal code.")
                    answerGiven = 0
                printAndPause("Mysterious Man: Continue on with my companion.")
            elif saveCode == "":
                print("Mysterious Man: Let's get you set up then.")
                startUp()
                answerGiven = 1
            else:
                printAndPause("Mysterious Man: That is an invalid save code.")
    else:
        startUp()
    clear()
    printAndPause("The Flipper: Welcome to the Casino! Let's gamble on a coin toss!")
    while money > 0:
        stake = 0
        bet = ""
        printAndPause(f"The Flipper: You currently have {money} flipcoin.")
        printAndPause("The Flipper: Do you want to bet on heads, tails, or landing on its edge?",0)
        bet = input("The Flipper: Odds: Heads - x1.9 your stake, Tails - x1.9 your stake, Edge - x500 your stake (Enter H for Heads, T for Tails or E for Edge) ")
        # check for valid stake
        while True:
            stake = input("The Flipper: How much do you want to bet? ")
            try:
                stake = int(stake)
            except ValueError:
                printAndPause("The Flipper: Please enter a valid input.")
                stake = 0
            else:
                stake = int(math.ceil(stake))
                if 0 < stake <= money: break
                printAndPause("The Flipper: That is an invalid stake.")
        if bet == "h":
            bet = "heads"
        elif bet == "t":
            bet = "tails"
        elif bet == "e":
            bet = "edge"
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
                printAndPause("The Flipper: Impressive. You won while betting on edge. Very brave of you.")
            if winInARow > 0:
                winInARow += 1
            else:
                winInARow = 1
            printAndPause(f"The Flipper: Wow! You won {winamount} flipcoin! Care to play again?")
            response = inputAndClear("The Flipper: Press 1 to play again, 2 to get your save code, 3 to view your trinkets and 4 to leave. ")
        else:
            if winInARow < 0 and bet != "edge":
                winInARow -= 1
            else:
                winInARow = -1
            printAndPause(f"The Flipper: Oh dear... It was {result}, you lost. Care to play again?")
            response = inputAndClear("The Flipper: Press 1 to play again, 2 to get your save code, 3 to view your trinkets and 4 to leave. ")
        if response == "4":
            response = inputAndClear("The Flipper: Are you sure you want to leave? Press 1 to return to the game, 2 to get your save code and leave and 3 to just leave. ")
            if response == "2":
                printAndPause(f"Mysterious Man: {saveCodeGenerator(money, trinketSave, trinkets, flips, oldManEncounters, oldManPower, winInARow, rubikssolved, wiseMessengerEncounters)}")
                break
            if response == "3":
                killScene = 1
                break
        if response == "2":
            printAndPause(f"Mysterious Man: {saveCodeGenerator(money, trinketSave, trinkets, flips, oldManEncounters, oldManPower, winInARow, rubikssolved, wiseMessengerEncounters)}")
        if response == "3":
            money = viewTrinkets(trinkets, flips, rubikssolved, money)
        #old man stuff
        if oldManPower > 0: oldManPower -= 1
        if random.randint(1,50) == 50:
            if oldManEncounters == 0:
                printAndPause("???: Psst... Hey Kid!",4)
                printAndPause("Wise Old Man: Kid, don't bet on edge, the odds are 1 in 5000!",4)
                printAndPause("Wise Old Man: These yung'uns could really use some help...",2)
                oldManEncounters += 1
            elif oldManEncounters == 1:
                printAndPause("Wise Old Man: Bet heads next time.",4)
                printAndPause("Wise Old Man: I promise you will win.",4)
                printAndPause("Wise Old Man: Give it everything you have.",2)
                oldManPower = 1
                oldManEncounters += 1
            elif oldManEncounters == 2:
                printAndPause("Wise Old Man: The Flipper is trying to 73696C656E6365 me.",4)
                printAndPause("Wise Old Man: I don't have long before I'm 676F6E650A.",4)
                printAndPause("Wise Old Man: Good Luck and bet on 6865616473 for the next 7468726565 goes.",4)
                oldManEncounters += 1
                oldManPower = 3
            elif oldManEncounters == 3:
                printAndPause("Old Man: Kid, I don't have lon-",4)
                printAndPause("The Flipper: Enough of this.",4)
                printAndPause("The Flipper: This knife'll do the trick...",4)
                printAndPause("*A curtain is drawn and st*bbing sounds are heard. When the curtain is pulled, the old man is nowhere to be seen.*",4)
                printAndPause("The Flipper: Good. Shall we continue?",4)
                oldManEncounters += 1
        #wise messenger
        if oldManEncounters >= 4 and flips >= 700 + (50 * wiseMessengerEncounters):
            if wiseMessengerEncounters == 0:
                printAndPause("???: You haven't met me before have you?",4)
                printAndPause("???: I've been brought here to free you from this loop.",4)
                printAndPause("Wise Messenger: I am the Wise Messenger.",4)
                wiseMessengerEncounters += 1
            elif wiseMessengerEncounters == 1:
                printAndPause("Wise Messenger: Why should you want escape you may ask...",4)
                printAndPause("Wise Messenger: You see, HE is evil. He's in it for the money only.",4)
                printAndPause("Wise Messenger: There's an old tale that his servant has killed more than 500 'robbers' as HE calls them.",4)
                printAndPause("Wise Messenger: Be Back Soon.",4)
                wiseMessengerEncounters += 2
            elif wiseMessengerEncounters == 3:
                printAndPause("Wise Messenger: If you want to escape his clutches, you will have to kill him.",4)
                printAndPause("Wise Messenger: I can help out with this quest but you will have to do the killing yourself.",4)
                #Key Event
                wiseMessengerHelp = inputAndClear("Wise Messenger: So, do you want to join me and slay HIM once and for all. (Yes or No) ")
                if wiseMessengerHelp.lower() == "yes":
                    wiseMessengerEncounters += 0.4
                else:
                    wiseMessengerEncounters += 0.1
            elif wiseMessengerEncounters == 3.1:
                printAndPause("Wise Messenger: Listen it would be better for both of us if you joined me to slay HIM.",4)
                wiseMessengerHelp = inputAndClear("Wise Messenger: So, do you want to join me and slay HIM once and for all. (Yes or No) ")
                if wiseMessengerHelp.lower() == "yes":
                    wiseMessengerEncounters = 3.4
                else:
                    printAndPause("Wise Messenger: If you so wish, I shall leave you to it. Enjoy being HIS puppet.",4)
            elif wiseMessengerEncounters == 3.4:
                pass

        #random dialogue bits
        if winInARow == 5 and _5FlipDialogue == 0:
            printAndPause("The Flipper: Someone's lucky today.")
            _5FlipDialogue = 1
        if winInARow == -5 and _5FlipDialogue2 == 0:
            printAndPause("The Flipper: Someone's unlucky today.")
            _5FlipDialogue2 = 1
        if winInARow == 10 and _10FlipDialogue == 0:
            printAndPause("The Flipper: Someone's extremely lucky toady.")
            _10FlipDialogue = 1
        if winInARow == -10 and _10FlipDialogue2 == 0:
            printAndPause("The Flipper: Someone's extremely unlucky today.")
            printAndPause(f"The Flipper: Here. A gift. 10% of your flipcoin.")
            printAndPause(f"The Flipper: Enjoy your {int(money*0.1)} flipcoin.")
            money = int(money*1.1)
        if money >= 1000 and _10FlipDialogue2 == 1 and taxDialogue == 0:
            printAndPause("The Flipper: Remember when I gave you some flipcoin?")
            printAndPause("The Flipper: I'll need some back. 10% to be exact.")
            money = round(money*0.9)
            taxDialogue = 1
        #trinkets
        if flips == 20 and "1" not in trinkets:
            printAndPause("The Flipper: Here. A trinket of thanks.")
            printAndPause("The Flipper: Enjoy my spider eye.")
            printAndPause("The Flipper: Keep it safe.")
            trinkets[0] = "1"
        if flips == 50 and "2" not in trinkets:
            printAndPause("The Flipper: Huh. You seem to really like playing.")
            printAndPause("The Flipper: Well... seen as you're still here...")
            printAndPause("The Flipper: Have this 'Keep on Flipping' poster.")
            trinkets[1] = "2"
        if flips == 100 and "3" not in trinkets:
            printAndPause("The Flipper: You seem to like hanging around here.")
            printAndPause("The Flipper: A puzzle, to pass the time...")
            printAndPause("The Flipper: You can have a Rubik's Cube keychain.")
            trinkets[2] = "3"
        if flips == 250 and "4" not in trinkets:
            printAndPause("The Flipper: You really are dedicated to this...")
            printAndPause("The Flipper: So I may as well award you.")
            printAndPause("The Flipper: You can have my half-eaten waffle.")
            trinkets[3] = "4"
        if flips == 1000 and "5" not in trinkets:
            printAndPause("The Flipper: You're our most loyal customer ever...")
            printAndPause("The Flipper: So here, an artifact older than time itself, something that has been handed down from generation to generation.",4)
            printAndPause("The Flipper: A golden spear.")
            trinkets[4] = "5"
        if flips >= 500 and oldManEncounters == 4 and "6" not in trinkets:
            printAndPause("The Flipper: You seem to really miss that old man...")
            printAndPause("The Flipper: Here. A memory of him. His skeleton.")
            printAndPause("The Flipper: He would have wanted you to have had it anyway.")
            trinkets[5] = "6"
        if random.randint(1,400) == 1 and "10" not in trinkets:
            printAndPause("The Flipper: Lucky.")
            printAndPause("The Flipper: Here. A Four Leaf Clover.")
            printAndPause("The Flipper: I've been told it's a symbol of luck.")
            trinkets[9] = "10"
        #Add more dialogue

    if killScene == 1 and money > 100:
        printAndPause("*As you begin to walk away you hear The Flipper bark orders at his servant.*",4)
        printAndPause("Servant: Must I?",4)
        printAndPause("*Suddenly you feel a sharp pain in the back of your head and you fall to the floor.*",8)
        printAndPause("The Flipper: The house. Always. WINS.",4)
        printAndPause("*As you feel yourself slipping away, The Flipper approaches and takes all your flipcoin, all the while with a manic smile.*",0)
    elif money > 0:
        printAndPause("The Flipper: Thanks for playing! See you again soon!",0)
    else:
        printAndPause("The Flipper: What a disappointing end...",2)
        printAndPause("The Flipper: Thanks for your money.",0)

if __name__ == "__main__":
    main()
