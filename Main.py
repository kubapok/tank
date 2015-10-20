import pygame, sys
from pygame.locals import *
from Tank import *


pygame.init()
FPS = 15 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
DISPLAYSURF = pygame.display.set_mode((900, 600), 0, 32)
pygame.display.set_caption('tank game')
WHITE = (255, 255, 255)

tank = Tank(100,100)
tracks = pygame.image.load('Images/tracks.png')
lake = pygame.image.load('Images/lake.png')
tree = pygame.image.load('Images/tree.png')

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if (tank.x == 300 and tank.y == 100) or\
        (tank.x == 100 and tank.y == 300) or\
        (tank.x == 300 and tank.y == 300) or\
        (tank.x == 100 and tank.y == 100):
        tank.turnRight()

    tank.move()

    #print(tank.direction)

    DISPLAYSURF.blit(tracks, (0, 0))
    DISPLAYSURF.blit(lake, (0, 0))
    DISPLAYSURF.blit(tree, (10, 10))
    DISPLAYSURF.blit(tank.lower, (tank.x, tank.y))
    DISPLAYSURF.blit(tank.upper, (tank.x, tank.y))

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
