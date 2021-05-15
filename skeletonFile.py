
import sys
import pygame

# SETUP

pygame.init()
pygame.display.set_caption(__file__)

# VARS

win = pygame.display.set_mode((640, 480))
width, height = pygame.display.get_window_size()
clock = pygame.time.Clock()

# LOOOOOOP

running = True
while running:
    win.fill((0, 0, 0)) # CLEAR

    for event in pygame.event.get(): # HANDLE EVENTS
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # DRAW AND UPDATE
    pygame.draw.rect(win, (255, 255, 255), (100, 100, 50, 50))
    pygame.display.flip()
    clock.tick(60)

# EXIT

pygame.quit()
sys.exit()
