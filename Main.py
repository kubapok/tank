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

train = Train(FPS)

def run_game(task):
    train_wait = -1
    while True:
        DISPLAYSURF.fill(WHITE)

        if task.value != 0: eval(Command.CommandIntToUser[task.value][1])
        task.value = 0

        if tank.rush:
            tank.move()

        for sheep in sheepes:
            sheep.move()
            sheep.turnIfCollide()


        for target in Target.targets:
            Target.detectCollison(target, tank)
            target.display(DISPLAYSURF)

        tank.display(DISPLAYSURF)

        train.move()
        train.display(DISPLAYSURF)

        #print(pygame.sprite.collide_mask(tree2, tank))

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


task = multiprocessing.Value('i',0) # sends command to game via integer number
game = multiprocessing.Process(target=run_game, args=(task,)) #
game.start()
command = Command()


while True:
    command.waitForCommand()
    if command.receivedFromUserEvent == True:
        task.value = command.task
        command.receivedFromUserEvent = False
