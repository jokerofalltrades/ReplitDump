import math
import time

from os import system

i = 1
global ExoticAntimatter

ExoticAntimatter = 10
FirstDimPrice = 10
FirstDim = 0
FirstDimMulti = 1
SecondDimPrice = 100
SecondDim = 0
SecondDimMulti = 1
FirstDimProduced = 0
ThirdDim = 0
ThirdDimMulti = 1
ThirdDimPrice = 10000
SecondDimProduced = 0
TickPrice = 1000
TickUpgrade = 0
Galaxies = 0
TickPower = 1
ThirdDimProduced = 0
FourthDim = 0
FourthDimPrice = 1000000
FourthDimMulti = 1
FourthDimProduced = 0
dimboosts = 0
FifthDim = 0
FifthDimPrice = 10000000
def clear():
	_ = system('clear')
while i > 0:
	if dimboosts < 1:
		time.sleep(TickPower)
		ExoticAntimatter = ExoticAntimatter + (
			(FirstDim + FirstDimProduced) * FirstDimMulti)
		FirstDimProduced = FirstDimProduced + (
			(SecondDim + SecondDimProduced) * SecondDimMulti)
		SecondDimProduced = SecondDimProduced + (
			(ThirdDim + ThirdDimProduced) * ThirdDimMulti)
		ThirdDimProduced = ThirdDimProduced + (FourthDim * FourthDimMulti)
		clear()
		print("You have " + str(ExoticAntimatter) + " Exotic Antimatter!")
		if FirstDimPrice > SecondDimPrice:
			SmallestPrice = SecondDimPrice
			if SmallestPrice > ThirdDimPrice:
				SmallestPrice = ThirdDimPrice
			if SmallestPrice > TickPrice:
				SmallestPrice = TickPrice
			if SmallestPrice > FourthDimPrice:
				SmallestPrice = FourthDimPrice
		else:
			SmallestPrice = FirstDimPrice
			if SmallestPrice > ThirdDimPrice:
				SmallestPrice = ThirdDimPrice
			if SmallestPrice > TickPrice:
				SmallestPrice = TickPrice
			if SmallestPrice > FourthDimPrice:
				SmallestPrice = FourthDimPrice
		if ExoticAntimatter >= SmallestPrice:
			inputs = input("Tickspeed x" + str(round(TickPower, 2)) + " Cost: " +
						str(TickPrice) + "\n" + "1st Dimension x" + str(FirstDimMulti) +
						" " + str(FirstDim+FirstDimProduced) + " (" + str(FirstDim) + ") Cost: " +
						str(FirstDimPrice) + "\n" + "2nd Dimension x" +
						str(SecondDimMulti) + " " + str(SecondDim+SecondDimProduced) + " (" +
						str(SecondDim) + ") Cost: " + str(SecondDimPrice) + "\n" +
						"3rd Dimension x" + str(ThirdDimMulti) + " " + str(ThirdDim+ThirdDimProduced) +
						" (" + str(ThirdDim) + ") Cost: " + str(ThirdDimPrice) +
						"\n" + "4th Dimension x" + str(FourthDimMulti) + " " +
						str(FourthDim+FourthDimProduced) + " (" + str(FourthDim) + ") Cost: " +
						str(FourthDimPrice)+"\n")
			if FourthDim >= 20:
				print("YOU CAN DIMBOOST! TYPE D TO RESET EVERYTHING AND UNLOCK A NEW DIMENSION (and a 2x boost to the 1st Dimension)")
			if inputs == "1":
				if ExoticAntimatter >= FirstDimPrice:
					FirstDim = FirstDim + 1
					ExoticAntimatter = ExoticAntimatter - FirstDimPrice
					if (FirstDim / 10) == math.ceil(FirstDim / 10):
						FirstDimMulti = FirstDimMulti * 2
						FirstDimPrice = FirstDimPrice * 1000
				else:
					print("You don't have enough Exotic Antimatter!")
			if inputs == "2":
				if ExoticAntimatter >= SecondDimPrice:
					SecondDim = SecondDim + 1
					ExoticAntimatter = ExoticAntimatter - SecondDimPrice
					if (SecondDim / 10) == math.ceil(SecondDim / 10):
						SecondDimMulti = SecondDimMulti * 2
						SecondDimPrice = SecondDimPrice * 10000
				else:
					print("You don't have enough Exotic Antimatter!")
			if inputs == "3":
				if ExoticAntimatter >= ThirdDimPrice:
					ThirdDim = ThirdDim + 1
					ExoticAntimatter = ExoticAntimatter - ThirdDimPrice
					if (ThirdDim / 10) == math.ceil(ThirdDim / 10):
						ThirdDimMulti = ThirdDimMulti * 2
						ThirdDimPrice = ThirdDimPrice * 100000
				else:
					print("You don't have enough Exotic Antimatter!")
			if inputs == "4":
				if ExoticAntimatter >= FourthDimPrice:
					FourthDim = FourthDim + 1
					ExoticAntimatter = ExoticAntimatter - FourthDimPrice
					if (FourthDim / 10) == math.ceil(FourthDim / 10):
						FourthDimMulti = FourthDimMulti * 2
						FourthDimPrice = FourthDimPrice * 1000000
				else:
					print("You don't have enough Exotic Antimatter!")
			if inputs == "t":
				if ExoticAntimatter >= TickPrice:
					if SecondDim > 0.5:
						ExoticAntimatter = ExoticAntimatter - TickPrice
						TickUpgrade = TickUpgrade + 1
						e = 0
						Galaxypower = 0
						while e < Galaxies:
							Galaxypower = Galaxypower + 0.01
							e += 1
						TickPower = (0.89 - Galaxypower)**TickUpgrade
						TickPrice = TickPrice * 10
				else:
					print("You don't have enough Exotic Antimatter!")
				if inputs == "d":
					if FourthDim >= 20:
						dimboosts = dimboosts + 1
		else:
			print("Tickspeed x" + str(round(TickPower, 2)) + " Cost: " +
						str(TickPrice) + "\n" + "1st Dimension x" + str(FirstDimMulti) +
						" " + str(FirstDim+FirstDimProduced) + " (" + str(FirstDim) + ") Cost: " +
						str(FirstDimPrice) + "\n" + "2nd Dimension x" +
						str(SecondDimMulti) + " " + str(SecondDim+SecondDimProduced) + " (" +
						str(SecondDim) + ") Cost: " + str(SecondDimPrice) + "\n" +
						"3rd Dimension x" + str(ThirdDimMulti) + " " + str(ThirdDim+ThirdDimProduced) +
						" (" + str(ThirdDim) + ") Cost: " + str(ThirdDimPrice) +
						"\n" + "4th Dimension x" + str(FourthDimMulti) + " " +
						str(FourthDim+FourthDimProduced) + " (" + str(FourthDim) + ") Cost: " +
						str(FourthDimPrice))
	
