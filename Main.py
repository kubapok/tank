#!/usr/bin/python3

import pygame, sys, random
from pygame.locals import *
import multiprocessing
#from multiprocessing import Process, Queue

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

    def go(distance):
        return ['tank.move()'] * (distance // tank.speed)

    def shoot():
        return ['tank.shoot()']

    def turnRight():
        return ['tank.turnRight()']

    def towerRight():
        return ['tank.towerRight()']

    def killHouse():
        newList = []
        for target in Target.targets:
            if  target.targetName == 'house':
                x,y = target.rect.x, target.rect.y
                if tank.rect.y > y and tank.direction == 'up':
                    print(tank.rect.y-y)
                    return go(tank.rect.y - y) + towerRight() + shoot() + ['print(tank.rect.y)']
                else:
                    return []


    train_wait = -1
    licznik = 300
    while True:
        if licznik: # nie wiem co to robi, ale boje sie na razie usunac
            licznik -= 1
        else:
            licznik = 300

        DISPLAYSURF.fill(YELLOW)

        if received.value:
            massage = UserInput.get()
            if massage == 'go':
                tasklist = go(50)
            elif massage == 'shoot':
                tasklist = shoot()
            elif massage == 'kill house':
                tasklist = killHouse()


            received.value = 0


        if tasklist != []: eval(tasklist.pop(0))


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

        for target in Target.targets:
            target.display(DISPLAYSURF)

        for flash in Destroyed.destroyed:
            flash.display(DISPLAYSURF)

        for bullet in Bullet.bullets:
            bullet.move()
            bullet.display(DISPLAYSURF)

        tank.display(DISPLAYSURF)

        train.move()
        train.display(DISPLAYSURF)


        ammobox.refillAmmoIfCollison(tank)
        ammobox.display(DISPLAYSURF)

        fuel.refillFuelIfCollison(tank)
        fuel.display(DISPLAYSURF)

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
