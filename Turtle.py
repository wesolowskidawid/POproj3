from Animal import Animal
import random

class Turtle(Animal):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 2, 1, xPos, yPos, "Turtle", "Zolw")
        self.setImage("Turtle.png")

    def action(self):
        chance = random.randint(0, 100)
        if chance > 75:
            super().action()

    def collision(self, opponent):
        if opponent.getStrength() < 5:
            opponent.move(-1, 0)
        else:
            super().collision(opponent)

