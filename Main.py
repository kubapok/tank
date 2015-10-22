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
tree = pygame.image.load('Images/tree.png')
lake = pygame.image.load('Images/lake.png')
train = pygame.image.load('Images/train.png')

class Tree():
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.image= pygame.image.load('Images/tree.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


tree2 = Tree(300,150)

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if (tank.x == 700 and tank.y == 100) or\
        (tank.x == 100 and tank.y == 700) or\
        (tank.x == 700 and tank.y == 700) or\
        (tank.x == 100 and tank.y == 100):
        tank.turnRight()

    tank.move()

    #print(tank.direction)

    DISPLAYSURF.blit(tracks, (0, 0))
    DISPLAYSURF.blit(lake, (0, 0))
    DISPLAYSURF.blit(tree, (10, 10))
    DISPLAYSURF.blit(tree2.image, (tree2.x, tree2.y))
    DISPLAYSURF.blit(train, (600, 50))
    DISPLAYSURF.blit(tank.lower, (tank.x, tank.y))
    DISPLAYSURF.blit(tank.upper, (tank.x, tank.y))


    #tank.update()
    print(pygame.sprite.collide_rect(tree2, tank))
    #print(tree2.rect)
    #print(tank.rect)
    #print(tank)

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
