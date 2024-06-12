from Animal import Animal


class CyberSheep(Animal):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 11, 4, xPos, yPos, "CyberSheep", "Cyber-Owca")
        self.setImage("CyberSheep.png")

    def action(self):
        from Hogweed import Hogweed
        hogweeds = [organism for organism in self.getWorld().organisms if isinstance(organism, Hogweed)]

        if hogweeds:
            closest_hogweed = min(hogweeds,
                                  key=lambda h: abs(h.getXPos() - self.getXPos()) + abs(h.getYPos() - self.getYPos()))
            hogweed_x = closest_hogweed.getXPos()
            hogweed_y = closest_hogweed.getYPos()

            if self.getXPos() < hogweed_x:
                move_x = 1
            elif self.getXPos() > hogweed_x:
                move_x = -1
            else:
                move_x = 0

            if self.getYPos() < hogweed_y:
                move_y = 1
            elif self.getYPos() > hogweed_y:
                move_y = -1
            else:
                move_y = 0

            self.move(move_x, move_y)

            if self.getXPos() == hogweed_x and self.getYPos() == hogweed_y:
                self.collision(closest_hogweed)
            elif self.getWorld().getOrganism(self.getXPos(), self.getYPos()):
                self.collision(self.getWorld().getOrganism(self.getXPos(), self.getYPos()))
        else:
            super().action()

    def collision(self, opponent):
        from Hogweed import Hogweed
        if isinstance(opponent, Hogweed):
            opponent.setAlive(False)
            self.getWorld().addInfo(self.getName() + " zjadła barszcz Sosnowskiego")
        else:
            super().collision(opponent)
