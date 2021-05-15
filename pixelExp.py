
'''

Pixel Engine
Nathan Vu, University of Oklahoma
5/14/2021

'''

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

pixel_size = 8
pixels = [[5, 2, 0, 0, 255]]

# LOOP

running = True
while running:
	win.fill((0, 0, 0)) # CLEAR

	for event in pygame.event.get(): # HANDLE EVENTS
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				running = False

	# ADD PIXELS
	pixels.append([
		random.randint(0, width) / pixel_size,
		random.randint(0, height) / pixel_size,
		0, 0, 255])

	# UPDATE AND DRAW
	for pixel in reversed(pixels): # 0x, 1y, 2vx, 3vy, 4a
		# MOVE
		pixel[3] += 1 # APPLY GRAVITY
		pixel[0] += pixel[2]
		pixel[1] += pixel[3]

		# COLLIDE
		if pixel[1] > (height / pixel_size):
			pixel[1] = height / pixel_size - 1

		# FADE AND REMOVE
		pixel[4] -= 5
		if pixel[4] < 1:
			pixels.remove(pixel)
			continue

		# DRAW
		s = pygame.Surface((pixel_size, pixel_size), pygame.SRCALPHA)
		s.fill((255, 255, 255, pixel[4]))
		win.blit(s, (
			pixel[0] * pixel_size,
			pixel[1] * pixel_size))

	pygame.display.flip()
	clock.tick(60)

pygame.quit()
sys.exit()
