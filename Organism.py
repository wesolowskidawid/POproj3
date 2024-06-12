from abc import ABC, abstractmethod
import random


class Organism(ABC):
    def __init__(self, world, strength, initiative, xPos, yPos, species, name):
        self._world = world
        self._strength = strength
        self._initiative = initiative
        self._xPos = xPos
        self._yPos = yPos
        self._age = 0
        self._isAlive = True
        self._breedingCooldown = 0
        self._maxBreedingCooldown = 20
        self._species = species
        self._name = name
        self._image = None

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def move(self, x, y):
        pass

    @abstractmethod
    def collision(self, opponent):
        pass

    def breed(self):
        from Antelope import Antelope
        from Belladonna import Belladonna
        from CyberSheep import CyberSheep
        from Fox import Fox
        from Grass import Grass
        from Guarana import Guarana
        from Hogweed import Hogweed
        from Sheep import Sheep
        from Sonchus import Sonchus
        from Turtle import Turtle
        from Wolf import Wolf
        direction = random.randint(0, 3)
        x = self.getXPos()
        y = self.getYPos()

        spawnx = 1
        spawny = 1
        canSpawn = False

        if direction == 0 and y < self.getWorld().getHeight()-1 and self.getWorld().getOrganism(x, y + 1) is None:
            spawnx = x
            spawny = y+1
            canSpawn = True
        elif direction == 1 and x < self.getWorld().getWidth()-1 and self.getWorld().getOrganism(x + 1, y) is None:
            spawnx = x+1
            spawny = y
            canSpawn = True
        elif direction == 2 and y > 0 and self.getWorld().getOrganism(x, y - 1) is None:
            spawnx = x
            spawny = y-1
            canSpawn = True
        elif direction == 3 and x > 0 and self.getWorld().getOrganism(x - 1, y) is None:
            spawnx = x-1
            spawny = y
            canSpawn = True

        if canSpawn:
            if self.getSpecies() == "Antelope":
                o = Antelope(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "Belladonna":
                o = Belladonna(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "CyberSheep":
                o = CyberSheep(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "Fox":
                o = Fox(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "Grass":
                o = Grass(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "Guarana":
                o = Guarana(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "Hogweed":
                o = Hogweed(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "Sheep":
                o = Sheep(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "Sonchus":
                o = Sonchus(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "Turtle":
                o = Turtle(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)
            elif self.getSpecies() == "Wolf":
                o = Wolf(self.getWorld(), spawnx, spawny)
                self.getWorld().addOrganism(o)

            self.setBreedingCooldown(self._maxBreedingCooldown)
            self.getWorld().addInfo(self.getName() + " rozmnożył się na polu " + str(spawnx) + " " + str(spawny) + "\n")

    def increaseAge(self):
        self._age += 1

    def getAge(self):
        return self._age

    def setAge(self, age):
        self._age = age

    def getBreedingCooldown(self):
        return self._breedingCooldown

    def setBreedingCooldown(self, cooldown):
        self._breedingCooldown = cooldown

    def decreaseBreedingCooldown(self):
        self._breedingCooldown -= 1

    def getStrength(self):
        return self._strength

    def setStrength(self, strength):
        self._strength = strength

    def getInitiative(self):
        return self._initiative

    def setInitiative(self, initiative):
        self._initiative = initiative

    def getXPos(self):
        return self._xPos

    def setXPos(self, xPos):
        self._xPos = xPos

    def getYPos(self):
        return self._yPos

    def setYPos(self, yPos):
        self._yPos = yPos

    def isAlive(self):
        return self._isAlive

    def setAlive(self, isAlive):
        self._isAlive = isAlive

    def getSpecies(self):
        return self._species

    def getName(self):
        return self._name

    def getWorld(self):
        return self._world

    def getImage(self):
        return self._image

    def setImage(self, imagePath):
        self._image = imagePath
