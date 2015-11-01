#!/usr/bin/python3

import multiprocessing

class Command():

    def __init__(self, ):
        self.receivedFromUserEvent = False
        self.task = None

    def waitForCommand(self):
        message = input()
        if message == 'rush':
            self.receivedFromUserEvent = True
            self.task = 1
        elif message == 'stop':
            self.receivedFromUserEvent = True
            self.task = 0
        elif message == 'right':
            self.receivedFromUserEvent = True
            self.task = 2
        elif message == 'left':
            self.receivedFromUserEvent = True
            self.task = 3
