#!/usr/bin/python3

import pygame, sys, random
from pygame.locals import *
import multiprocessing
import colorama
import sys
import time
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
from Command import *

pygame.init()
colorama.init

FPS = 30
WHITE = (255, 255, 255)
YELLOW = (200,200,0)
#ERRORDISPLAY = 1
WIDTH = 900
HEIGHT = 600

fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((900, 600), 0, 32)
pygame.display.set_caption('tank game')



def gamePrint(text):
    print(colorama.Fore.YELLOW + text + colorama.Style.RESET_ALL)

def make_trees(trees,quantity,min_x,max_x,min_y,max_y):
    for t in range(quantity):
        trees.append(Tree(  int(random.random()*(max_x-min_x)) + min_x,
                            int(random.random()*(max_y-min_y)) + min_y,
                            'light' if random.random() > 0.5 else 'dark'
                            ))


tank = Tank(300,500)
lake = Lake(0,0)
path = Path(0,0)
tracks = Tracks(0,0)
house = House(610, 240)

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


introText = '''\
Welcome to the tank simulation game. You control
the tank via this command line. Type a command
in natural language to give an order.
Type one command at a time. You can use either
simple and more complex sentences.
You don't have any particular goal to achieve.
Just make some noise and try to feel like
a real tank crewman.
'''

def run_game(userInput,received,isDead):
    tasklist = []

    while True:
        if received.value:
            massage = UserInput.get()
            if massage == 'exit':
                pygame.quit()
                sys.exit()

            received.value = 0
            if tank.exist:
                if len(tasklist) != 0:
                    gamePrint('Aborting current action')
                tasklist = eval('Tasks.' + massage) if massage else []


        if tank.exist and tasklist != []: eval(tasklist.pop(0))

        if random.random() < 0.0005: make_trees(trees,1,0,400,0,200)
        if random.random() < 0.0005: make_trees(trees,1,0,180,300,480)

        for sheep in sheepes:
            sheep.move()
            sheep.turnIfCollide()

        for target in Target.targets:
            if tank.exist and Target.detectCollison(target, tank):
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

        ammobox.refillAmmoIfCollison(tank)
        ammobox.display(DISPLAYSURF)

        fuel.refillFuelIfCollison(tank)
        fuel.display(DISPLAYSURF)

        if tank.exist == True:
            tank.detectWaterCollision(lake)
            tank.display(DISPLAYSURF)
        else:
            if tank.youDiedMassage == False:
                gamePrint("Sorry, You died.")
                gamePrint("Type anything to exit")
                isDead.value = 1
                tasklist = []
                tank.youDiedMassage = True

        train.move()
        train.display(DISPLAYSURF)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
        pygame.display.update()
        fpsClock.tick(FPS)


UserInput = multiprocessing.Queue()
received = multiprocessing.Value('i',0)
isDead = multiprocessing.Value('i',0)

game = multiprocessing.Process(target=run_game, args=(UserInput,received,isDead,))
game.start()

gamePrint(introText)
while True:

    if isDead.value == 1:
        gamePrint("Sorry, you died. You can't give any orders")
        gamePrint("Type anything to exit")
        UserInput.put('exit')
        received.value = 1
        sys.exit()

    massage = input()
    if massage:
        if massage == 'exit' and isDead.value == 0:
            UserInput.put('exit')
            received.value = 1
            sys.exit()
            break
        if isDead.value == 0:
            command = Command(massage)
            sendToGame = command.interpret()
            received.value = 1
            UserInput.put(sendToGame)
