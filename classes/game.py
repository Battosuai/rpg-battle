import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, magic, attack, defence):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.attackLow = attack - 10
        self.attackHigh = attack + 10
        self.defence = defence
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def genrateDamage(self):
        return random.randrange(self.attackLow, self.attackHigh)

    def generateSpellDamage(self, i):
        magicLow = self.magic[i]["damage"] - 5
        magicHigh = self.magic[i]["damage"] + 5
        return random.randrange(magicLow, magicHigh)

    def takeDamage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def getHp(self):
        return self.hp

    def getMaxHp(self):
        return self.maxHp

    def getMp(self):
        return self.mp

    def getMaxMp(self):
        return self.maxMp

    def reduceMp(self, cost):
        self.mp -= cost
        if self.mp < 0:
            self.mp = 0
        return self.mp

    def getSpellName(self, i):
        return self.magic[i]["name"]

    def getSpellCost(self, i):
        return self.magic[i]["cost"]

    def chooseAction(self):
        i = 1
        print(bcolors.OKBLUE+bcolors.BOLD+"Actions"+bcolors.ENDC)
        for item in self.actions:
            print(str(i)+":"+item)
            i += 1

    def chooseMagic(self):
        i = 1
        print(bcolors.OKBLUE+bcolors.BOLD+"Magics"+bcolors.ENDC)
        for item in self.magic:
            print(str(i)+":"+item["name"], "(cost:"+item["cost"]+")")
            i += 1
