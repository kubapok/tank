#!/usr/bin/python3
import random
from Tank import *

def go(distance, tank):
    return ['tank.move()'] * (distance // tank.speed)

def wait():
    return ['tank.wait()'] * 30  # FPS value

def shoot():
    return ['tank.shoot()']

def turnRight():
    return ['tank.turnRight()']

def turnLeft():
    return ['tank.turnLeft()']

def towerRight():
    return ['tank.towerRight()']

def towerLeft():
    return ['tank.towerLeft()']

def rideOver(name, tank, targets):
    print(Tank.ammo)
    newList = []
    target = None
    for item in targets:
        print(item.targetName)
        #nonlocal target
        if  item.targetName == name:
            target = item
            break
    assert target.targetName == name
    x,y = target.rect.x  , target.rect.y
    print(item.targetName,x,y)
    print(tank.rect.x, tank.rect.y)

    if tank.aim == tank.direction:
        pass
    elif tank.aim == Tank.toLeft[tank.direction]:
        newList += towerRight()
    elif tank.aim == Tank.toRight[tank.direction]:
        newList += towerLeft()
    else:
        if random.random() < 0.5:
            newList += towerLeft() + wait() + towerLeft()
        else:
            newList += towerRight() + wait() + towerRight()

    newList += wait()

    if tank.rect.y > y: #czolg jest pod
        if tank.direction == 'up':
            pass
        elif tank.direction == 'down':
            newList += turnRight()
            newList += wait()
            newList += turnRight()
        elif tank.direction == 'left':
            newList += turnRight()
        elif tank.direction == 'right':
            newList += turnLeft()
        else:
            assert False
    elif tank.rect.y <= y: #czolg jest nad
        if tank.direction == 'up':
            newList += turnRight()
            newList += wait()
            newList += turnRight()
        elif tank.direction == 'down':
            pass
        elif tank.direction == 'left':
            newList += turnLeft()
        elif tank.direction == 'right':
            newList += turnRight()
        else:
            assert False

    newList += wait()

    print('going:',abs(tank.rect.y - y))
    newList += go(abs(tank.rect.y - y), tank)

    # STARA POZYCJA CZOŁGU
    if tank.rect.x < x:
        if tank.rect.y > y: # czolg jest pod
            newList += turnRight()
        elif tank.rect.y < y:
            newList += turnLeft()
        else:
            assert False
    elif tank.rect.x >= x:
        if tank.rect.y > y: # czolg jest nad
            newList += turnLeft()
        elif tank.rect.y <= y:#!!!!!!!!!!!!!!!!!!
            newList += turnRight()
        else:
            assert False
    else:
        assert False

    newList += wait()

    print('going: ',abs(x - tank.rect.x))
    newList += go(abs(x - tank.rect.x), tank)
    return newList


def shootTarget(name, tank, targets):
    target = None
    newList = []
    for item in targets:
        print(item.targetName)
        if  item.targetName == name:
            target = item
            break
    assert target.targetName == name
    x,y = target.rect.x - target.image.get_rect().centerx // 2 , target.rect.y - target.image.get_rect().centery //2
    print(item.targetName,x,y)
    print(tank.rect.x, tank.rect.y)


    if tank.aim == tank.direction:
        pass
    elif tank.aim == Tank.toLeft[tank.direction]:
        newList += towerRight()
    elif tank.aim == Tank.toRight[tank.direction]:
        newList += towerLeft()
    else:
        if random.random() < 0.5:
            newList += towerLeft() + wait() + towerLeft()
        else:
            newList += towerRight() + wait() + towerRight()

    newList += wait()



    if tank.rect.y > y: #czolg jest pod
        if tank.direction == 'up':
            pass
        elif tank.direction == 'down':
            newList += turnRight()
            newList += wait()
            newList += turnRight()
        elif tank.direction == 'left':
            newList += turnRight()
        elif tank.direction == 'right':
            newList += turnLeft()
        else:
            assert False
    elif tank.rect.y <= y: #czolg jest nad
        if tank.direction == 'up':
            newList += turnRight()
            newList += wait()
            newList += turnRight()
        elif tank.direction == 'down':
            pass
        elif tank.direction == 'left':
            newList += turnLeft()
        elif tank.direction == 'right':
            newList += turnRight()
        else:
            assert False

    newList += wait()
    print('going:',abs(tank.rect.y - y))
    newList += go(abs(tank.rect.y - y), tank)

    # STARA POZYCJA CZOŁGU
    if tank.rect.x < x:
        if tank.rect.y > y: # czolg jest pod
            newList += towerRight()
        elif tank.rect.y <= y:
            newList += towerLeft()
        else:
            assert False
    elif tank.rect.x >= x:
        if tank.rect.y >= y: # czolg jest nad
            newList += towerLeft()
        elif tank.rect.y < y:
            newList += towerRight()
        else:
            assert False
    else:
        assert False

    newList += wait()
    newList += shoot()
    return newList

def refillAmmo(tank, targets):
    return rideOver('ammo', tank, targets)

def refillFuel(tank, targets):
    return rideOver('fuel', tank, targets)
