#!/usr/bin/python3

import pygame, sys, random, multiprocessing
from pygame.locals import *

from Tank import *
from Tree import *
from Train import *
from Lake import *
from Tracks import *
from Sheep import *
from Fence import *
from Command import *

pygame.init()

FPS = 30
WHITE = (255, 255, 255)
#ERRORDISPLAY = 1
max_train_wait = 30 # maximum time we can wait for new train after old one is gone
WIDTH = 900
HEIGHT = 600

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((900, 600), 0, 32)
pygame.display.set_caption('tank game')



tank = Tank(100,100)
tree1 = Tree(10,10)
tree2 = Tree(300,150)
lake = Lake(0,0)
tracks = Tracks(0,0)

sheepes = [ #XD
    Sheep(800,390, 'left'),
    Sheep(820,450, 'left'),
    Sheep(750,500, 'right'),
    Sheep(890,430, 'right'),
    Sheep(900,480, 'right')
]

fences = [
    Fence(770,550,2),
    Fence(700,500,1),
    Fence(650,450,2),
    Fence(640,380,3),
    Fence(685,325,4),
    Fence(770,300,5),
    Fence(855,310,6)
]



def run_game():
    while True:
        DISPLAYSURF.fill(WHITE)
        '''
        if (tank.rect.x == 300 and tank.rect.y == 100) or\
            (tank.rect.x == 100 and tank.rect.y == 300) or\
            (tank.rect.x == 300 and tank.rect.y == 300) or\
            (tank.rect.x == 100 and tank.rect.y == 100):
            tank.turnRight()

        tank.move()
        '''
        '''
        print(command.receivedFromUserEvent.is_set())
        if command.receivedFromUserEvent.is_set():
            tank.move()
        '''
        for sheep in sheepes:
            sheep.move()
            sheep.turnIfCollide()

        tracks.display(DISPLAYSURF)
        tree1.display(DISPLAYSURF)
        tree2.display(DISPLAYSURF)
        lake.display(DISPLAYSURF)
        tank.display(DISPLAYSURF)

        if (Train.exists == True):
            train.move()
            train.display(DISPLAYSURF)
        else:
            try:
                train_wait -= 1
            except NameError:
                train_wait = int(random.random()* FPS * max_train_wait)
            if train_wait < 0:
                train = Train(2)
                train_wait = int(random.random()* FPS * max_train_wait)

        for fence in fences:
            fence.display(DISPLAYSURF)
        for sheep in sheepes:
            sheep.display(DISPLAYSURF)

        #print(pygame.sprite.collide_mask(tree2, tank))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


game = multiprocessing.Process(target=run_game)
game.start()

while True:
    command = Command()
    while not command.receivedFromUserEvent.is_set():
        command.waitForCommand()
    print('command received')
    tank.move()
