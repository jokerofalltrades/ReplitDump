import pygame
import sys
from pygame.locals import *

# Constants
KEY_SIZE = 100
GRID_ROWS, GRID_COLS = 2, 3
WINDOW_WIDTH, WINDOW_HEIGHT = KEY_SIZE * GRID_COLS, KEY_SIZE * GRID_ROWS
KEYS = ["ESC", "UP", "SPACE", "LEFT", "DOWN", "RIGHT"]
KEYSNAMES = ["ESC", "↑", "␣", "←", "↓", "→"]

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Input Display')
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)

def render_key(key, x, y, active):
    """Render a key on the grid."""
    color = GREEN if active else GRAY
    rect = pygame.Rect(x, y, KEY_SIZE, KEY_SIZE)
    pygame.draw.rect(window, color, rect)
    pygame.draw.rect(window, BLACK, rect, 2)  # Border
    text = font.render(KEYSNAMES[KEYS.index(key)], True, BLACK)
    text_rect = text.get_rect(center=rect.center)
    window.blit(text, text_rect)

def main():
    # Key states
    key_states = {key: False for key in KEYS}
    while True:
        window.fill(WHITE)
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: key_states["ESC"] = True
                if event.key == pygame.K_UP: key_states["UP"] = True
                if event.key == pygame.K_DOWN: key_states["DOWN"] = True
                if event.key == pygame.K_LEFT: key_states["LEFT"] = True
                if event.key == pygame.K_RIGHT: key_states["RIGHT"] = True
                if event.key == pygame.K_SPACE: key_states["SPACE"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE: key_states["ESC"] = False
                if event.key == pygame.K_UP: key_states["UP"] = False
                if event.key == pygame.K_DOWN: key_states["DOWN"] = False
                if event.key == pygame.K_LEFT: key_states["LEFT"] = False
                if event.key == pygame.K_RIGHT: key_states["RIGHT"] = False
                if event.key == pygame.K_SPACE: key_states["SPACE"] = False
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                pygame.quit()
                sys.exit()
        # Render keys in a 3x2 grid
        for i, key in enumerate(KEYS):
            x = (i % GRID_COLS) * KEY_SIZE
            y = (i // GRID_COLS) * KEY_SIZE
            render_key(key, x, y, key_states[key])
        pygame.display.update()

if __name__ == "__main__":
    main()