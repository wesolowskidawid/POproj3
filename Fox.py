from Animal import Animal
import random


class Fox(Animal):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 3, 7, xPos, yPos, "Fox", "Lis")
        self.setImage("Fox.png")

    def action(self):
        direction = random.randint(0, 3)

        if direction == 0:
            if self.getYPos() < self.getWorld().getHeight()-1:
                opponent = self.getWorld().getOrganism(self.getXPos(), self.getYPos() + 1)
                if opponent is not None and opponent.getStrength() <= self.getStrength():
                    self.collision(opponent)
                    self.move(0, 1)
                elif opponent is None:
                    self.move(0, 1)
        elif direction == 1:
            if self.getXPos() < self.getWorld().getWidth()-1:
                opponent = self.getWorld().getOrganism(self.getXPos() + 1, self.getYPos())
                if opponent is not None and opponent.getStrength() <= self.getStrength():
                    self.collision(opponent)
                    self.move(1, 0)
                elif opponent is None:
                    self.move(1, 0)
        elif direction == 2:
            if self.getYPos() > 0:
                opponent = self.getWorld().getOrganism(self.getXPos(), self.getYPos() - 1)
                if opponent is not None and opponent.getStrength() <= self.getStrength():
                    self.collision(opponent)
                    self.move(0, -1)
                elif opponent is None:
                    self.move(0, -1)
        elif direction == 3:
            if self.getXPos() > 0:
                opponent = self.getWorld().getOrganism(self.getXPos() - 1, self.getYPos())
                if opponent is not None and opponent.getStrength() <= self.getStrength():
                    self.collision(opponent)
                    self.move(-1, 0)
                elif opponent is None:
                    self.move(-1, 0)