
import pygame
import sys
import random
import math

# CLASSES
class Part:
    def __init__(self, x, y, r, a):
        self.x = x
        self.y = y
        self.r = r
        self.a = a
        self.dead = False

    def tick(self):
        self.a += 0.05
        self.x += math.cos(self.a)
        self.y += math.sin(self.a)
        self.r -= 0.1
        if self.r < 0:
            self.dead = True

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.r)

# SETUP
pygame.init()
pygame.display.set_caption(__file__)

# VARS
win = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
width, height = pygame.display.get_window_size()
parts = []

ex = 0
ey = 0
a = 0

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

    # ADD PARTS
    a += 0.1
    ex = width / 2 + math.cos(a) * 100
    ey = height / 2 + math.sin(a) * 100
    for deg in range(0, 360, 36):
        parts.append(Part(
            ex,
            ey,
            5,
            deg * math.pi / 180
        ))

    # UPDATE AND DRAW
    for part in reversed(parts):
        part.tick()
        part.draw(win)
        if part.dead:
            parts.remove(part)
    
    pygame.display.flip()
    clock.tick(60)
    
