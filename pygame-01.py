#	----------------------------------
#		My simple pygame program
#	----------------------------------

import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Run program
running = True
while running:

    # Events
    for event in pygame.event.get():
		# Keysboard keys hits
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

		# [X] btn
		elif event.type == QUIT:
            running = False



    screen.fill((255, 255, 255))

    surf = pygame.Surface((50, 50))

    surf.fill((0, 0, 0))
	rect = surf.get_rect()


pygame.quit()