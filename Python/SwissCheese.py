import random
import sys

import pygame
from pygame.locals import QUIT

o = 0
swisscheese = []

pygame.init()
window = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Swiss Cheese')
while True:
  pygame.Surface.fill(window, (255, 176, 0))

  def createholes(numberofholes):
    a = 0
    holelocations = []
    while a < numberofholes:
      holesize = random.randint(1, 10)
      holelocationx = (random.randint(1, (101 - holesize)))
      holelocationy = (random.randint(1, (101 - holesize)))
      i = 0
      modifier = 0
      while i < holesize:
        e = 0
        while e < holesize:
          holelocations.append((holelocationy * 101 + holelocationx) +
                               modifier)
          e = e + 1
          modifier = modifier + 1
        i = i + 1
        modifier = modifier + (101 - holesize)
      a = a + 1
    return holelocations

  def drawholes():
    i = 0
    for i in range(10201):
      if swisscheese[i] == 0:
        mod = 3
        firstx = int((i % 101) * mod) - mod
        firsty = int(((i - i % 101) / 101) * mod) - mod
        pygame.draw.rect(window, (0, 0, 0), (firstx, firsty, mod, mod))
    pygame.display.update()

  numberofholes = int(input("How many holes should there be?"))
  pygame.Surface.fill(window, (255, 176, 0))
  o = 0
  swisscheese.clear()
  holelocations = createholes(numberofholes)
  while o < 10201:
    if o in holelocations:
      swisscheese.append(0)
    else:
      swisscheese.append(1)
    o = o + 1

  drawholes()

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  pygame.display.update()
