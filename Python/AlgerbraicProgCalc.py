max = int(input("What's the current cap? "))
maxprod = 0
vals = []
for a in range(max):
    for c in range(max):
        if (max**2)/4 - (a+1)*(c+1) > 0:
            if (max*(c+1))**((a+1)/2-0.5) > maxprod:
                maxprod = (max*(c+1))**((a+1)/2-0.5)
                vals = [(a+1), max, (c+1)]
print(f"The maximmum production is {maxprod}, with a being {vals[0]}, b being {vals[1]} and c being {vals[2]}.")