#!/usr/bin/python3

import multiprocessing

class Command():

    CommandIntToUser = []
    CommandIntToUser.append([None,None])
    CommandIntToUser.append(['stop','tank.setRush(False)'])
    CommandIntToUser.append(['rush','tank.setRush(True)'])
    CommandIntToUser.append(['right','tank.turnRight()'])
    CommandIntToUser.append(['left','tank.turnLeft()'])
    CommandIntToUser.append(['towerLeft','tank.towerLeft()'])
    CommandIntToUser.append(['towerRight','tank.towerRight()'])

    def waitForCommand(self):
        message = input()

        try:
            self.task = [x[0] for x in Command.CommandIntToUser].index(message)
            print('Command received')
        except ValueError:
            print('Repeat command, please')

        self.receivedFromUserEvent = True
