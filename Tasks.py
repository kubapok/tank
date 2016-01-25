#!/usr/bin/python3
import random, colorama
from Tank import *
from Command import Command

colorama.init()

def taskPrint(text, complex = False):
    if complex:
        print(colorama.Fore.RED + 'Objective: '  + colorama.Style.RESET_ALL + str(text))
    else:
        print(colorama.Fore.GREEN + 'Task: '  + colorama.Style.RESET_ALL + str(text))

def go(distance, tank):
    if distance == Command.inftyDistance:
        taskPrint('rushing')
    else:
        taskPrint('going ' + str(distance) + ' units of length')
    return ['tank.move()'] * (distance // tank.speed)

def wait():
    return ['tank.wait()'] * 30  # FPS value

def stop():
    taskPrint('stopping')
    return []

def shoot():
    taskPrint('shooting')
    return ['tank.shoot()']

def turnRight():
    taskPrint('turning right')
    return ['tank.turnRight()']

def turnLeft():
    taskPrint('turning left')
    return ['tank.turnLeft()']

def towerRight():
    taskPrint('turning turret right')
    return ['tank.towerRight()']

def towerLeft():
    taskPrint('turning turret left')
    return ['tank.towerLeft()']

def back():
    taskPrint('turning back')
    if random.random() < 0.5:
        return ['tank.turnLeft()'] +\
            wait() +\
            ['tank.turnLeft()']
    else:
        return ['tank.turnRight()'] +\
            wait() +\
            ['tank.turnRight()']

def rideOver(name, tank, targets, nearest = False):
    assert nearest in [True, False]
    newList = []
    target = None

    if nearest == True:
        for item in targets:
            if item.targetName == name:
                if target == None or abs(tank.rect.x - item.rect.x) + abs(tank.rect.y - item.rect.y) <\
                                            abs(tank.rect.x - target.rect.x) + abs(tank.rect.y - target.rect.y):
                    target = item

    elif nearest == False:
        for item in targets:
                if  item.targetName == name:
                    target = item
                    break

    if not target.targetName in {'ammo', 'fuel'}:
        taskPrint('riding over the ' + target.targetName, complex = True)

    assert target.targetName == name
    x,y = target.rect.x  , target.rect.y

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

    newList += go(abs(tank.rect.y - y), tank)

    # STARA POZYCJA CZOŁGU
    if tank.rect.x < x:
        if tank.rect.y > y: # czolg jest pod
            newList += turnRight()
        elif tank.rect.y <= y:
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

    newList += go(abs(x - tank.rect.x), tank)
    return newList


def shootTarget(name, tank, targets, nearest = False):
    assert nearest in [True, False]
    newList = []
    target = None

    if nearest == True:
        for item in targets:
            if item.targetName == name:
                if target == None or abs(tank.rect.x - item.rect.x) + abs(tank.rect.y - item.rect.y) <\
                                            abs(tank.rect.x - target.rect.x) + abs(tank.rect.y - target.rect.y):
                    target = item

    elif nearest == False:
        for item in targets:
            if  item.targetName == name:
                target = item
                break

    assert target.targetName == name
    taskPrint('shooting the ' + target.targetName, complex = True)
    x,y = target.rect.x - target.image.get_rect().centerx // 2 , target.rect.y - target.image.get_rect().centery //2


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
    taskPrint('refilling ammo', complex = True)
    return rideOver('ammo', tank, targets)

def refillFuel(tank, targets):
    taskPrint('refilling fuel', complex = True)
    return rideOver('fuel', tank, targets)
