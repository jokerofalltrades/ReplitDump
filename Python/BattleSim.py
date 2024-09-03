import random
import math
level=1
def main(level):
    global health
    global enemyhp
    health=math.ceil(level*10)
    enemyhp=int(math.ceil(health*(random.randint(math.ceil(level*50),math.ceil(level*int(110+level*10)))/100)))
    combat(enemyhp,health,level)
def combat(enemyhp,health,level):
    print(str("You have "+str(health)+" health. Your Enemy has "+str(enemyhp)+" health."))
    inputs=input("What do you do? a for attack, r to run and h to heal 10% of your current health")
    if health<0.5:
        print("You lost!")
        main(level)
    maxenemydamage = math.ceil(health*40/100)
    if maxenemydamage < int(0.5):
        maxenemydamage = 1
    if inputs == "a":
        CheckIfPlayerHits(enemyhp,health,level,maxenemydamage)
    else:
        if inputs == "r":
            main(level)
        else:
            if inputs == "h":
                health=math.ceil(health*1.1)
                enemydamage=math.ceil(random.randint(health*0/100,maxenemydamage))
                print("Your enemy deals "+str(enemydamage)+" damage.")
                health=health-enemydamage
                combat(enemyhp,health,level)
            else:
                print("That is not a valid input")
                enemydamage=math.ceil(random.randint(health*0/100,maxenemydamage))
                print("Your enemy deals "+str(enemydamage)+" damage.")
                health=health-enemydamage
                combat(enemyhp,health,level)
    enemydamage=math.ceil(random.randint(health*0/100,maxenemydamage))
    print("Your enemy deals "+str(enemydamage)+" damage.")
    health=health-enemydamage
def CheckIfPlayerHits(enemyhp,health,level,maxenemydamage):
    move=random.randint(1,100)
    if move>15:
        if math.ceil((level+1)/2) - (level+1)/2 > int(0.5):
            difference = 1 - (math.ceil((level+1)/2) - (level+1)/2)
            multiplier = math.ceil(((level+1)/2) - difference)
        else:
            multiplier = math.ceil((level+1)/2)
        damage=(random.randint(2,5)*multiplier)
        print("Your attack deals "+str(damage)+" damage.")
        enemyhp=enemyhp-damage
        enemydamage=math.ceil(random.randint(health*0/100,maxenemydamage))
        print("Your enemy deals "+str(enemydamage)+" damage.")
        health=health-enemydamage
    else:
        print("Your attack misses!")
        enemydamage=math.ceil(random.randint(health*0/100,maxenemydamage))
        if enemydamage > 0:
          print("Your enemy deals "+str(enemydamage)+" damage.")
        else:
          print("Your enemy misses.")
        health=health-enemydamage
    if enemyhp>0:
        combat(enemyhp,health,level)
    else:
        print("You win!")
        level=level+0.1
        main(level)
main(level)
