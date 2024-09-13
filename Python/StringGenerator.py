import random
endofu=random.randint(30,100)
u=0
story=""
letters =  ["","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
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
        word=word+letters[letternumber]
    else:
        sentence=sentence+" "+word
  else:
      sentence=sentence+"."
      story=story+" "+sentence
else:
  print(story)
