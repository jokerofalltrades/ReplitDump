import random
endofu=random.randint(30,100)
u=0
story=""
while endofu>u:
  u=u+1
  endofe=random.randint(2,20)
  e=0
  sentence=""
  while endofe>e:
    e=e+1
    i=0
    endofi=random.randint(3,12)
    word=""
    while endofi>i:
        i=i+1
        letternumber=random.randint(1,26)
        if letternumber==1:
            word=word+"a"
        if letternumber==2:
            word=word+"b"
        if letternumber==3:
            word=word+"c"
        if letternumber==4:
            word=word+"d"
        if letternumber==5:
            word=word+"e"
        if letternumber==6:
            word=word+"f"
        if letternumber==7:
            word=word+"g"
        if letternumber==8:
            word=word+"h"
        if letternumber==9:
            word=word+"i"
        if letternumber==10:
            word=word+"j"
        if letternumber==11:
            word=word+"k"
        if letternumber==12:
            word=word+"l"
        if letternumber==13:
            word=word+"m"
        if letternumber==14:
            word=word+"n"
        if letternumber==15:
            word=word+"o"
        if letternumber==16:
            word=word+"p"
        if letternumber==17:
            word=word+"q"
        if letternumber==18:
            word=word+"r"
        if letternumber==19:
            word=word+"s"
        if letternumber==20:
            word=word+"t"
        if letternumber==21:
            word=word+"u"
        if letternumber==22:
            word=word+"v"
        if letternumber==23:
            word=word+"w"
        if letternumber==24:
            word=word+"x"
        if letternumber==25:
            word=word+"y"
        if letternumber==26:
            word=word+"z"
    else:
        sentence=sentence+" "+word
  else:
      sentence=sentence+"."
      story=story+" "+sentence
else:
  print(story)
