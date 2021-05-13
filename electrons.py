
import sys
import pygame
import random
import math

# CLASSES
class Electron:
    def __init__(self, x, y, s, vx, vy, r, g, b):
        self.x = x   # pos
        self.y = y
        self.s = s   # size
        self.vx = vx # velocity
        self.vy = vy
        self.r = r   # color
        self.g = g
        self.b = b

    def tick(self, width, height):
        cx = width / 2 # find point 1
        cy = height / 2
        dx = self.x - cx # find delta pos
        dy = self.y - cy
        rad = math.atan2(dy, dx) + math.pi # find angle
        self.vx += math.cos(rad) # accelerate
        self.vy += math.sin(rad)
        self.x += self.vx # move
        self.y += self.vy

    def draw(self, win):
        pygame.draw.circle(win, (self.r, self.g, self.b), (self.x, self.y), self.s)

# SETUP
pygame.init()
pygame.display.set_caption(__file__)

# VARS
rands = lambda: -1 if random.random() < 0.5 else 1
win = pygame.display.set_mode((640, 480))
width, height = pygame.display.get_window_size()
clock = pygame.time.Clock()
electrons = []

# ADD ELECTRONS
for _ in range(25):
    electrons.append(Electron(
        random.randint(0, width),
        random.randint(0, height),
        3,
        0,
        0,
        random.random() * 255,
        random.random() * 255,
        random.random() * 255
    ))

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

    # DRAW AND UPDATE
    for electron in reversed(electrons):
        electron.tick(width, height)
        electron.draw(win)
    
    pygame.display.flip()
    clock.tick(60)

# EXIT
pygame.quit()
sys.exit()
