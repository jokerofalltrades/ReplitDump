import random
import sys
import pygame
from pygame.locals import QUIT

# Constants
WINDOW_SIZE = 300
GRID_SIZE = 101
PIXEL_COUNT = GRID_SIZE * GRID_SIZE
PIXEL_SIZE = 3
CHEESE_COLOR = (255, 176, 0)
HOLE_COLOR = (0, 0, 0)

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Swiss Cheese')

def create_holes(number_of_holes):
    hole_locations = []
    for _ in range(number_of_holes):
        hole_size = random.randint(1, 10)
        hole_x = random.randint(0, GRID_SIZE - hole_size)
        hole_y = random.randint(0, GRID_SIZE - hole_size)
        for i in range(hole_size):
            for j in range(hole_size):
                hole_locations.append((hole_y + i) * GRID_SIZE + (hole_x + j))
    return hole_locations

def draw_holes(swiss_cheese):
    for i in range(PIXEL_COUNT):
        if swiss_cheese[i] == 0:
            x = (i % GRID_SIZE) * PIXEL_SIZE
            y = (i // GRID_SIZE) * PIXEL_SIZE
            pygame.draw.rect(window, HOLE_COLOR, (x, y, PIXEL_SIZE, PIXEL_SIZE))
    pygame.display.update()

def main():
    while True:
        window.fill(CHEESE_COLOR)
        try:
            number_of_holes = int(input("How many holes should there be? "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        swiss_cheese = [1] * PIXEL_COUNT
        hole_locations = create_holes(number_of_holes)
        for loc in hole_locations:
            swiss_cheese[loc] = 0

        draw_holes(swiss_cheese)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()