#!/usr/bin/python3
import colorama
colorama.init()

def commandPrint(text):
    #print(text)
    print(colorama.Fore.YELLOW + text + colorama.Style.RESET_ALL)
class Command():

    TargetNames = {'house',
                    'sheep',
                    'tree',
                    'boat',
                    'train',
                    'tree',
                    'fence'
    }

    #thats funny: if i specify 99999999 fps is very low
    inftyDistance = 999

    import Synonyms
    shootSynonyms       = Synonyms.shoot
    rideSynonyms        = Synonyms.ride
    refillSynonyms      = Synonyms.refill
    ammoSynonyms        = Synonyms.ammo
    fuelSynonyms        = Synonyms.fuel
    backSynonyms        = Synonyms.back
    goSynonyms          = Synonyms.go
    killSynonyms        = Synonyms.kill


    def __init__(self, massage):
        massage=massage.replace('?',' ?')
        massage=massage.replace('.',' .')
        massage=massage.replace(',',' ,')
        self.text = set(massage.lower().split())




        #SHOOT STH
    def interpret(self):
        #shoot a target
        if Command.shootSynonyms.intersection(self.text):
            if Command.TargetNames.intersection(self.text):
                return "shootTarget('"+ Command.TargetNames.intersection(self.text).pop() +"', tank, Target.targets)"


        #JUST SHOOT
        if Command.shootSynonyms.intersection(self.text):
            return"shoot()"

        #RIDE OVER STH
        if Command.rideSynonyms.intersection(self.text):
            if Command.TargetNames.intersection(self.text):
                return "rideOver('"+ Command.TargetNames.intersection(self.text).pop() +"', tank, Target.targets)"


        #KILL STH
        if Command.killSynonyms.intersection(self.text):
            if len(Command.TargetNames.intersection(self.text))==0:
                commandPrint("What should I " + Command.killSynonyms.intersection(self.text).pop() + '?')
                whatToKill = set(input().lower().split())
                self.text.update(whatToKill)
                return self.interpret()#returning THIS function
            commandPrint ("Tell me how I should " + Command.killSynonyms.intersection(self.text).pop() + ' '+Command.TargetNames.intersection(self.text).pop()+ '.')
            howToKill = set(input().lower().split())
            self.text.update(howToKill)
            return self.interpret()
            #no return here, the command will be grabber by SHOOT STH OR RIDE OVER STH



        #DO STH WITH TARGET BUT NO ACTION NOT SPECIFIED
        if Command.TargetNames.intersection(self.text):
            commandPrint("What should I do with " + Command.TargetNames.intersection(self.text).pop()+ " ?")
            what = set(input().lower().split())
            self.text.update(what)
            return self.interpret()


        #REFILL AMMO OR FUEL
        if Command.refillSynonyms.intersection(self.text):
            if Command.ammoSynonyms.intersection(self.text):
                return "refillAmmo(tank, Target.targets)"
            if Command.fuelSynonyms.intersection(self.text):
                return "refillFuel(tank, Target.targets)"
            commandPrint ("Tell me what I should " + Command.refillSynonyms.intersection(self.text).pop() +'.')
            whatToRefill = set(input().lower().split())
            if Command.ammoSynonyms.intersection(whatToRefill):
                return "refillAmmo(tank, Target.targets)"
            if Command.fuelSynonyms.intersection(whatToRefill):
                return "refillFuel(tank, Target.targets)"

        #TURRET TO LEFT OR RIGHT
        if 'turret' in self.text:
            if 'left' in self.text:
                return 'towerLeft()'
            if 'right' in self.text:
                return 'towerRight()'
            commandPrint('Which direction should I turn that turret at?')

        #TURN LEFT
        if 'left' in self.text:
            return 'turnLeft()'
        #TURN RIGHT
        if 'right' in self.text:
            return 'turnRight()'

        #TURN BACK
        if Command.backSynonyms.intersection(self.text):
            return 'back()'

        #GO SPECIFIED DISTANCE OR JUST GO
        if Command.goSynonyms.intersection(self.text):
            digitList = [x for x in self.text if x.isdigit()]
            if len(digitList) == 1:
                return 'go(' + digitList[0] + ',tank)'
            else:
                return 'go(' + str(Command.inftyDistance) + ',tank)'

        commandPrint('Can You repeat, please?')
        return []
