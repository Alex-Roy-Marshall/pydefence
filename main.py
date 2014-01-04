import os, sys, pygame
from os.path import dirname
from pygame import transform
'''
Created on 3 Jan 2014

@author: Katie.Clark
'''
DIRNAME = os.path.join(dirname(__file__), 'resources',)
SCREEN_SIZE = width, height = 800, 600
CAPTION = 'PyDefense'

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE))
    pygame.display.set_caption(CAPTION)

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = pygame.image.load(os.path.join(DIRNAME, 'images', 'map.gif'))
    #background = transform.scale(background, SCREEN_SIZE)
    background = background.convert()
    background.fill((0, 250, 0))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    
    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:sys.exit()
        screen.blit(background, (0, 0))

if __name__ == '__main__':
    main()