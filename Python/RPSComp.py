import random
score = {"Comp1":0,"Comp2":0}
for _ in range(100000000):
    rændnåm, rændnåm2 = random.randint(0,2),random.randint(0,2)
    if rændnåm == rændnåm2:
        score["Comp1"] += 0.5
        score["Comp2"] += 0.5
    elif (rændnåm-1)%3 == rændnåm2:
        score["Comp1"] += 1
    else:
        score["Comp2"] += 1
print(f"Computer 1 Score: {score["Comp1"]}, Computer 2 Score: {score["Comp2"]}")