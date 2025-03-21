import random

allpoems = ["Ozymandias","London","Prelude","Last Duchess","COLB","Exposure","Storm","Bayonet Charge","Remains","Poppies","War Photographer","Tissue","Emigree","COMH","Kamikaze"]
Poems = {
    "Ozymandias":["Exposure","Storm","Last Duchess","Prelude"],
    "London":["Prelude","Emigree","COMH","Tissue"],
    "Prelude":["Ozymandias","London","Storm","Kamikaze"],
    "Last Duchess":["COMH","Ozymandias"],
    "COLB":["Poppies","Remains","War Photographer","Bayonet Charge","Exposure"],
    "Exposure":["Ozymandias","COLB","Remains"],
    "Storm":["Prelude","Bayonet Charge","London","Emigree"],
    "Bayonet Charge":["COLB","Storm","Remains","War Photographer"],
    "Remains":["COLB","Exposure","Bayonet Charge","War Photographer","Poppies","Kamikaze"],
    "Poppies":["Kamikaze","War Photographer","Remains","COLB"],
    "War Photographer":["Remains","Bayonet Charge","Kamikaze"],
    "Tissue":["Ozymandias","Poppies"],
    "Emigree":["Poppies","London","Kamikaze","Storm"],
    "COMH":["London","Tissue"],
    "Kamikaze":["COMH","Poppies","Prelude","Remains"]
}
bestlists = []
bestlen = 15
for i in range(10000):
    comparedto = []
    poemspicked = set()
    while len(comparedto) < 15:
        poemtopick = random.randint(0,14)
        if allpoems[poemtopick] not in poemspicked:
            poemspicked.add(allpoems[poemtopick])
            for poem in Poems[allpoems[poemtopick]]:
                if poem not in comparedto:
                    comparedto.append(poem)
    if len(poemspicked) < bestlen:
        bestlists.clear()
        bestlists.append(poemspicked)
        bestlen = len(poemspicked)
    elif len(poemspicked) == bestlen and poemspicked not in bestlists:
        bestlists.append(poemspicked)
for sets in bestlists:
    print(sets)
print(bestlen)