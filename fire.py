
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

# LOOP

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

    # ADD
    parts.append([
        width / 2,
        height / 2,
        random.random() * rands() * 0.5,
        -random.random() * 2,
        random.randint(10, 20),
        random.randint(0, 255)
    ])

    # UPDATE AND DRAW
    for part in reversed(parts):
        # x, y, vx, vy, s, g
        part[0] += part[2]
        part[1] += part[3]
        part[4] -= 0.25
        if part[4] < 1:
            parts.remove(part)
            continue
        pygame.draw.rect(win, (255, part[5], 0), (
            part[0] - part[4] / 2,
            part[1] - part[4] / 2,
            part[4], part[4]))
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
