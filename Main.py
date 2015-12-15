#!/usr/bin/python3

import pygame, sys, random
from pygame.locals import *
import multiprocessing
#from multiprocessing import Process, Queue

import Tasks

from Tank import *
from Tree import *
from Train import *
from Lake import *
from Tracks import *
from Sheep import *
from Fence import *
from Boat import *
from Path import *
from House import *

pygame.init()

FPS = 30
WHITE = (255, 255, 255)
YELLOW = (200,200,0)
#ERRORDISPLAY = 1
WIDTH = 900
HEIGHT = 600

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((900, 600), 0, 32)
pygame.display.set_caption('tank game')

tank = Tank(300,500)
lake = Lake(0,0)
path = Path(0,0)
tracks = Tracks(0,0)
house = House(610, 240)

def make_trees(trees,quantity,min_x,max_x,min_y,max_y):
    for t in range(quantity):
        trees.append(Tree(  int(random.random()*(max_x-min_x)) + min_x,
                            int(random.random()*(max_y-min_y)) + min_y,
                            'light' if random.random() > 0.5 else 'dark'
                            ))

trees = []
make_trees(trees,30,0,400,0,200)
make_trees(trees,15,0,180,300,480)


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

boats = [
    Boat(800,10),
    Boat(700,30, pos = 'right')
]

train = Train(FPS)

ammobox = AmmoBox(25, 530)
fuel = Fuel(110, 530)


def run_game(userInput,received):
    tasklist = []
    #train_wait = -1
    #licznik = 300
    while True:
        '''
        if licznik: # nie wiem co to robi, ale boje sie na razie usunac
            licznik -= 1
        else:
            licznik = 300
        '''

        if received.value and tank.exist:
            massage = UserInput.get()
            if massage == 'go':
                tasklist = Tasks.go(50, tank)
            elif massage == 'turn right':
                tasklist = Tasks.turnRight()
            elif massage == 'turn left':
                tasklist = Tasks.turnLeft()
            elif massage == 'tower right':
                tasklist = TaskstowerRight()
            elif massage == 'tower left':
                tasklist = Tasks.towerLeft()
            elif massage == 'shoot':
                tasklist = Tasks.shoot()
            elif massage == 'kill house':
                tasklist = Tasks.rideOver('house', tank, Target.targets, nearest = True)
            elif massage == 'kill sheep':
                tasklist = Tasks.rideOver('sheep', tank, Target.targets, nearest = True)
            elif massage == 'kill tree':
                tasklist = Tasks.rideOver('tree', tank, Target.targets, nearest = True)
            elif massage == 'kill all trees':
                tasklist = Tasks.killAll('tree', tank, Target.targets)
            elif massage == 'kill boat':
                tasklist = Tasks.rideOver('boat', tank, Target.targets)
            elif massage == 'kill train':
                tasklist = Tasks.rideOver('train', tank, Target.targets)
            elif massage == 'shoot house':
                tasklist = Tasks.shootTarget('house', tank, Target.targets)
            elif massage == 'shoot sheep':
                tasklist = Tasks.shootTarget('sheep', tank, Target.targets)
            elif massage == 'shoot tree':
                tasklist = Tasks.shootTarget('tree', tank, Target.targets)
            elif massage == 'shoot boat':
                tasklist = Tasks.shootTarget('boat', tank, Target.targets)
            elif massage == 'refill ammo':
                tasklist = Tasks.refillAmmo(tank, Target.targets)
            elif massage == 'refill fuel':
                tasklist= Tasks.refillFuel(tank, Target.targets)
            received.value = 0

        if tasklist != []: eval(tasklist.pop(0))

        if random.random() < 0.0005: make_trees(trees,1,0,400,0,200)
        if random.random() < 0.0005: make_trees(trees,1,0,180,300,480)

        for sheep in sheepes:
            sheep.move()
            sheep.turnIfCollide()

        for target in Target.targets:
            if Target.detectCollison(target, tank):
                Target.delete(target)
            for bullet in Bullet.bullets:
                if Target.detectCollison(target, bullet):
                    Target.delete(target)
                    bullet.remove()

        DISPLAYSURF.fill(YELLOW)

        for target in Target.targets:
            target.display(DISPLAYSURF)

        for flash in Destroyed.destroyed:
            flash.display(DISPLAYSURF)

        for bullet in Bullet.bullets:
            bullet.move()
            bullet.display(DISPLAYSURF)

        tank.detectWaterCollision(lake)


        ammobox.refillAmmoIfCollison(tank)
        ammobox.display(DISPLAYSURF)

        fuel.refillFuelIfCollison(tank)
        fuel.display(DISPLAYSURF)

        if tank.exist == True:
            tank.display(DISPLAYSURF)
        else:
            if tank.youDiedMassage == False:
                print('You died, sorry')
                tank.youDiedMassage = True

        train.move()
        train.display(DISPLAYSURF)

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


UserInput = multiprocessing.Queue()
received = multiprocessing.Value('i',0)
game = multiprocessing.Process(target=run_game, args=(UserInput,received,))
game.start()

while True:
    massage = input()
    if massage:
        received.value = 1
        UserInput.put(massage)
