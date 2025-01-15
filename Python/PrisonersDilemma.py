import math
import random

BOTHCOOP = 2
BOTHCHEAT = 0
CHEAT = 3
COOP = -1
strats = ["TFT", "TFTT", "ACO", "ACH", "RAND", "WSLS"]
# Cooperate = 0 Cheat = 1
def TitForTat(oppLastMove, moveNum):
    myMove = oppLastMove if moveNum != 0 else 0
    return myMove

def TitForTwoTats(oppLastLastMove, oppLastMove, moveNum):
    myMove = oppLastMove if moveNum != 0 and (oppLastLastMove == oppLastMove) else 0
    return myMove

def AlwaysCoop():
    myMove = 0
    return myMove

def AlwaysCheat():
    myMove = 1
    return myMove

def Random():
    myMove = random.randint(0, 1)
    return myMove

def WinStayLoseSwitch(oppLastMove, myLastMove, moveNum):
    myMove = (myLastMove if moveNum != 0 and oppLastMove == 0 
              else 1 if myLastMove == 0 else 0)
    return myMove

def SimulateInteractions(nOfMoves, nOfPlayers):
    for v in range(nOfPlayers**2):
        Player1 = math.floor(v / nOfPlayers)
        Player2 = v % nOfPlayers
        if Player1 != Player2:
            Player1Strat = strats[Player1 - 1]
            Player2Strat = strats[Player2 - 1]
            Player1LastMove = None
            Player2LastMove = None
            Player1LastLastMove = None
            Player2LastLastMove = None
            Player1Score = 0
            Player2Score = 0
            Player1Move = None
            Player2Move = None
            for i in range(nOfMoves):
                if Player1Strat == "TFT":
                    Player1Move = TitForTat(Player2LastMove, i)
                if Player1Strat == "TFTT":
                    Player1Move = TitForTwoTats(Player2LastLastMove, Player2LastMove, i)
                if Player1Strat == "ACO":
                    Player1Move = AlwaysCoop()
                if Player1Strat == "ACH":
                    Player1Move = AlwaysCheat()
                if Player1Strat == "RAND":
                    Player1Move = Random()
                if Player1Strat == "WSLS":
                    Player1Move = WinStayLoseSwitch(Player2LastMove, Player1LastMove, i)
                if Player2Strat == "TFT":
                    Player2Move = TitForTat(Player1LastMove, i)
                if Player2Strat == "TFTT":
                    Player2Move = TitForTwoTats(Player1LastLastMove, Player1LastMove, i)
                if Player2Strat == "ACO":
                    Player2Move = AlwaysCoop()
                if Player2Strat == "ACH":
                    Player2Move = AlwaysCheat()
                if Player2Strat == "RAND":
                    Player2Move = Random()
                if Player2Strat == "WSLS":
                    Player2Move = WinStayLoseSwitch(Player1LastMove, Player2LastMove, i)
                if Player1Move == 0:
                    if Player2Move == 0:
                        Player1Score += BOTHCOOP
                        Player2Score += BOTHCOOP
                    else:
                        Player1Score += COOP
                        Player2Score += CHEAT
                else:
                    if Player2Move == 0:
                        Player1Score += CHEAT
                        Player2Score += COOP
                    else:
                        Player1Score += BOTHCHEAT
                        Player2Score += BOTHCHEAT
                Player1LastLastMove = Player1LastMove
                Player1LastMove = Player1Move
                Player2LastLastMove = Player2LastMove
                Player2LastMove = Player2Move
            print(f"{Player1Strat} vs {Player2Strat}: {Player1Score} - {Player2Score}")

SimulateInteractions(100, 6)