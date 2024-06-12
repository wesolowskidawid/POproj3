from Animal import Animal
import random


class Antelope(Animal):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 4, 4, xPos, yPos, "Antelope", "Antylopa")
        self.setImage("Antelope.png")

    def action(self):
        super().action()
        super().action()

    def collision(self, opponent):
        chance = random.randint(1, 100)
        if chance < 50:
            super().collision(opponent)
