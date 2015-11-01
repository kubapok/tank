import multiprocessing

class Command():

    def __init__(self, ):
        self.receivedFromUserEvent = multiprocessing.Event()

    def waitForCommand(self):
        if input() != '':
            self.receivedFromUserEvent.set()
