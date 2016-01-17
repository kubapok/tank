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
    shootSynonyms = Synonyms.shoot
    rideSynonyms = Synonyms.ride
    refillSynonyms = Synonyms.refill
    ammoSynonyms = Synonyms.ammo
    fuelSynonyms = Synonyms.fuel


    def __init__(self, massage):
        massage=massage.replace('?',' ?')
        massage=massage.replace('.',' .')
        massage=massage.replace(',',' ,')
        self.text = set(massage.lower().split())


    def interpret(self):
        if Command.shootSynonyms.intersection(self.text):
            if Command.TargetNames.intersection(self.text):
                return "shootTarget('"+ Command.TargetNames.intersection(self.text).pop() +"', tank, Target.targets)"

        if Command.rideSynonyms.intersection(self.text):
            if Command.TargetNames.intersection(self.text):
                return "rideOver('"+ Command.TargetNames.intersection(self.text).pop() +"', tank, Target.targets)"

        if Command.refillSynonyms.intersection(self.text):
            if Command.ammoSynonyms.intersection(self.text):
                return "refillAmmo(tank, Target.targets)"
            if Command.fuelSynonyms.intersection(self.text):
                return "refillFuel(tank, Target.targets)"
            print ("Tell me what I should " + Command.refillSynonyms.intersection(self.text).pop())
            return []
        print('Can You repeat, please?')
        return []
