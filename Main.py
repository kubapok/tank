#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

from Tank import *
from Tree import *
from Train import *
from Lake import *
from Tracks import *
from Sheep import *
from Fence import *

pygame.init()


FPS = 90
WHITE = (255, 255, 255)
ERRORDISPLAY = 1


fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((900, 600), 0, 32)
pygame.display.set_caption('tank game')


tank = Tank(100,100)
tree1 = Tree(10,10)
tree2 = Tree(300,150)
train = Train()
lake = Lake(0,0)
tracks = Tracks(0,0)


sheepes = [ #XD
    Sheep(800,400),
    Sheep(850,450)
]


fences = [
    Fence(770,550,2),
    Fence(700,500,1),
    Fence(650,450,2),
    Fence(640,380,3),
    Fence(685,325,4),
    Fence(770,300,5),
    Fence(855,330,6)
]

while True:
    DISPLAYSURF.fill(WHITE)

    if (tank.rect.x == 300 and tank.rect.y == 100) or\
        (tank.rect.x == 100 and tank.rect.y == 300) or\
        (tank.rect.x == 300 and tank.rect.y == 300) or\
        (tank.rect.x == 100 and tank.rect.y == 100):
        tank.turnRight()
        #tank.towerLeft()

    tank.move()
    train.move()

    tracks.display(DISPLAYSURF)
    tree1.display(DISPLAYSURF)
    tree2.display(DISPLAYSURF)
    lake.display(DISPLAYSURF)
    train.display(DISPLAYSURF)
    tank.display(DISPLAYSURF)


    for fence in fences:
        fence.display(DISPLAYSURF)

    for sheep in sheepes:
        sheep.display(DISPLAYSURF)

    print(pygame.sprite.collide_mask(tree2, tank))


    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
