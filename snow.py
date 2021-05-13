
import sys
import pygame
import random

# SETUP
pygame.init()
pygame.display.set_caption(__file__)

# VARS
rands = lambda: -1 if random.random() < 0.5 else 1
win = pygame.display.set_mode((640, 480))
width, height = pygame.display.get_window_size()
clock = pygame.time.Clock()
parts = []

# LOOOOOOP
running = True
while running:
    win.fill((0, 0, 0))

    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # ADD PARTS
    parts.append([
        random.randint(0, width),
        -10,
        random.random() * rands(),
        random.randint(1, 5),
        random.randint(1, 5)
    ])

    # DRAW AND UPDATE
    for part in reversed(parts):
        # 0x, 1y, 2vx, 3vy, 4r
        part[0] += part[2]
        part[1] += part[3]
        pygame.draw.circle(win, (255, 255, 255), (part[0], part[1]), part[4])
        if part[1] - part[4] > height:
            parts.remove(part)
    
    pygame.display.flip()
    clock.tick(60)

# EXIT
pygame.quit()
sys.exit()
