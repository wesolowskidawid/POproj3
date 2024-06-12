from Organism import Organism
import random


class Plant(Organism):
    def __init__(self, world, strength, initiative, xPos, yPos, species, name):
        super().__init__(world, strength, initiative, xPos, yPos, species, name)

    def move(self, x, y):
        pass

    def action(self):
        chance = random.randint(1, 100)
        tries = 1
        if self.getSpecies() == "Sonchus":
            tries = 3

        for i in range(tries):
            if self.getAge() > 10 and chance > 95 and self.getBreedingCooldown() == 0:
                self.breed()
            chance = random.randint(1, 100)

    def collision(self, opponent):
        pass

    