from Plant import Plant
from Organism import Organism
import random


class Animal(Organism):
    def __init__(self, world, strength, initiative, xPos, yPos, species, name):
        super().__init__(world, strength, initiative, xPos, yPos, species, name)

    def move(self, x, y):
        x0 = self._xPos
        y0 = self._yPos

        self.setXPos(x0 + x)
        self.setYPos(y0 + y)

        self.getWorld().addInfo(self.getName() + " przesuwa się z pola " + str(x0) + " " + str(y0) + " na pole " + str(self.getXPos()) + " " + str(self.getYPos()) + "\n")

    def action(self):
        # every animal moves in a random direction every turn
        direction = random.randint(0, 3)

        if direction == 0:
            if self.getYPos() < self.getWorld().getHeight()-1:
                if self.getWorld().getOrganism(self.getXPos(), self.getYPos() + 1) is not None:
                    self.collision(self.getWorld().getOrganism(self.getXPos(), self.getYPos() + 1))
                self.move(0, 1)
        elif direction == 1:
            if self.getYPos() > 0:
                if self.getWorld().getOrganism(self.getXPos(), self.getYPos() - 1) is not None:
                    self.collision(self.getWorld().getOrganism(self.getXPos(), self.getYPos() - 1))
                self.move(0, -1)
        elif direction == 2:
            if self.getXPos() < self.getWorld().getWidth()-1:
                if self.getWorld().getOrganism(self.getXPos() + 1, self.getYPos()) is not None:
                    self.collision(self.getWorld().getOrganism(self.getXPos() + 1, self.getYPos()))
                self.move(1, 0)
        elif direction == 3:
            if self.getXPos() > 0:
                if self.getWorld().getOrganism(self.getXPos() - 1, self.getYPos()) is not None:
                    self.collision(self.getWorld().getOrganism(self.getXPos() - 1, self.getYPos()))
                self.move(-1, 0)

    def collision(self, opponent):
        from Human import Human
        chance = random.randint(1, 100)

        if isinstance(opponent, Plant):
            opponent.collision(self)
        elif isinstance(opponent, Human):
            opponent.collision(self)
        elif self.getSpecies() == opponent.getSpecies():
            if self.getAge() > 10 and opponent.getAge() > 10 and chance > 95 and self.getBreedingCooldown() == 0 and opponent.getBreedingCooldown() == 0:
                self.breed()
        else:
            if self.getStrength() >= opponent.getStrength():
                self.getWorld().addInfo(self.getName() + " zabił " + opponent.getName() + " na polu " + str(opponent.getXPos()) + " " + str(opponent.getYPos()) + "\n")
                opponent.setAlive(False)
            else:
                self.getWorld().addInfo(opponent.getName() + " zabił " + self.getName() + " na polu " + str(opponent.getXPos()) + " " + str(opponent.getYPos()) + "\n")
                self.setAlive(False)
