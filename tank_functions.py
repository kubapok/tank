#!/usr/bin/python3

from Target import *
from Tank import *

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
                return go(tank.rect.y - y) + towerRight() + shoot()
            else:
                return []
