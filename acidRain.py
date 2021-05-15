
import sys
import random
import pygame

# SETUP

pygame.init()
pygame.display.set_caption(__file__)

# VARS

win = pygame.display.set_mode((640, 480))
width, height = pygame.display.get_window_size()
clock = pygame.time.Clock()
drop_size = 8
drops = []
timer = 0
step = 1
cd = 5

# LOOOOOOP

running = True
while running:
    # CLEAR
    s = pygame.Surface((width, height), pygame.SRCALPHA)
    s.fill((0, 0, 0, 255 / 4))
    win.blit(s, (0, 0))

    # HANDLE EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # ADDING
    timer += step
    if timer > cd:
        timer = 0
        drops.append([
            random.randint(0, width),
            random.randint(-50, -10),
            random.random(),
            random.randint(3, 7)
        ])

    # DRAW AND UPDATE
    for drop in reversed(drops): # 0x, 1y, 2vx, 3vy

        # MOVE
        drop[0] += drop[2]
        drop[1] += drop[3]

        # DIE
        if drop[1] > height:
            drops.remove(drop)
            continue

        # DRAW
        pygame.draw.rect(win, (0, 0, 255), (
            drop[0],
            drop[1],
            drop_size,
            drop_size
        ))

    pygame.display.flip()
    clock.tick(60)

# EXIT

pygame.quit()
sys.exit()
