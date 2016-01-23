#!/usr/bin/python3

class Command():

    TargetNames = {'house',
                    'sheep',
                    'tree',
                    'boat',
                    'train',
                    'tree',
                    'fence'
    }

    import Synonyms
    shootSynonyms       = Synonyms.shoot
    rideSynonyms        = Synonyms.ride
    refillSynonyms      = Synonyms.refill
    ammoSynonyms        = Synonyms.ammo
    fuelSynonyms        = Synonyms.fuel
    backSynonyms        = Synonyms.back
    goSynonyms          = Synonyms.go


    def __init__(self, massage):
        massage=massage.replace('?',' ?')
        massage=massage.replace('.',' .')
        massage=massage.replace(',',' ,')
        self.text = set(massage.lower().split())


    def interpret(self):
        #SHOOT STH
        if Command.shootSynonyms.intersection(self.text):
            if Command.TargetNames.intersection(self.text):
                return "shootTarget('"+ Command.TargetNames.intersection(self.text).pop() +"', tank, Target.targets)"
            else:
                return "shoot()"

        #RIDE OVER STH
        if Command.rideSynonyms.intersection(self.text):
            if Command.TargetNames.intersection(self.text):
                return "rideOver('"+ Command.TargetNames.intersection(self.text).pop() +"', tank, Target.targets)"

        #REFILL AMMO OR FUEL
        if Command.refillSynonyms.intersection(self.text):
            if Command.ammoSynonyms.intersection(self.text):
                return "refillAmmo(tank, Target.targets)"
            if Command.fuelSynonyms.intersection(self.text):
                return "refillFuel(tank, Target.targets)"
            print ("Tell me what I should " + Command.refillSynonyms.intersection(self.text).pop())
            return []

        #TURRET TO LEFT OR RIGHT
        if 'turret' in self.text:
            if 'left' in self.text:
                return 'towerLeft()'
            if 'right' in self.text:
                return 'towerRight()'
            print('Which direction should I turn that turret at?')

        #TURN LEFT
        if 'left' in self.text:
            return 'turnLeft()'
        #TURN RIGHT
        if 'right' in self.text:
            return 'turnRight()'

        #TURN BACK
        if Command.backSynonyms.intersection(self.text):
            return 'back()'

        if Command.goSynonyms.intersection(self.text):
            digitList = [x for x in self.text if x.isdigit()]
            if len(digitList) == 1:
                #return 'go(15,tank)'
                return 'go(' + digitList[0] + ',tank)'



        print('Can You repeat, please?')
        return []
