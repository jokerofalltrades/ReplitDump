import pygame
import math
import numpy as np
pygame.init()
screen = pygame.display.set_mode((640, 480))
def drawRegularPolygon(surface, color, numSides, tiltAngle, x, y, radius, returns = False):
    pts = []
    for i in range(numSides):
        x = x + radius * math.cos(tiltAngle + math.pi * 2 * i / numSides)
        y = y + radius * math.sin(tiltAngle + math.pi * 2 * i / numSides)
        pts.append([int(x), int(y)])
    pygame.draw.polygon(surface, color, pts)
    if returns: return pts

pts = drawRegularPolygon(screen, (255, 0, 0), 6, 0, 100, 100, 200, True)
print(pts)
for i in range(len(pts)-1):
    print(round(-(pts[1+i][1]-pts[0+i][1])/(pts[1+i][0]-pts[0+i][0]),2))
while True:
    if pygame.event.get(pygame.QUIT):
        break
    pygame.display.update()