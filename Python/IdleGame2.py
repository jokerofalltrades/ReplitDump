import time

hydrogen = 0
hydrogenPerSecond = 1
hydrogenProductionMulti = 1
helium = 0

def calculate(hydrogen, hydrogenPerSecond, hydrogenProductionMulti):
  hydrogenProductionRate = round(hydrogenPerSecond / 10 * hydrogenProductionMulti, 2)
  hydrogen = round(hydrogen + hydrogenProductionRate,2)
  return hydrogen, hydrogenProductionRate

def printEverything(hydrogen, hydrogenProductionRate):
  print("Hydrogen: "+str(hydrogen)+" ("+str(hydrogenProductionRate*10)+ "/s)",end="\r")
  #print("Helium: " + str(hydrogen) + " (" + str(hydrogenProductionRate) + "/s)")

while True:
  hydrogen, hydrogenProductionRate = calculate(hydrogen, hydrogenPerSecond,
hydrogenProductionMulti)
  printEverything(hydrogen, hydrogenProductionRate)
  time.sleep(0.1) 
