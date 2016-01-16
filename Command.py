#!/usr/bin/python3

class Command():

    TargetNames = {'house',
                    'sheep',
                    'tree',
                    'boat',
                    'train',
                    'tree'

    }


    def __init__(self, massage):
        massage=massage.replace('?',' ?')
        massage=massage.replace('.',' .')
        massage=massage.replace(',',' ,')
        self.text = set(massage.lower().split())
        print(self.text)


    def interpret(self):
        if 'shoot' in self.text:
            if Command.TargetNames.intersection(self.text):
                return "shootTarget('"+ Command.TargetNames.intersection(self.text).pop() +"', tank, Target.targets)"
        if 'ride' in self.text:
            if Command.TargetNames.intersection(self.text):
                return "rideOver('"+ Command.TargetNames.intersection(self.text).pop() +"', tank, Target.targets)"
