from Plant import Plant

class Hogweed(Plant):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 10, 0, xPos, yPos, "Hogweed", "Barszcz sosnowskiego")
        self.setImage("Hogweed.png")

    def action(self):
        x = self.getXPos()
        y = self.getYPos()

        if self.getWorld().getOrganism(x, y-1) is not None:
            self.getWorld().getOrganism(x, y-1).setAlive(False)
        if self.getWorld().getOrganism(x, y+1) is not None:
            self.getWorld().getOrganism(x, y+1).setAlive(False)
        if self.getWorld().getOrganism(x-1, y) is not None:
            self.getWorld().getOrganism(x-1, y).setAlive(False)
        if self.getWorld().getOrganism(x+1, y) is not None:
            self.getWorld().getOrganism(x+1, y).setAlive(False)

        super().action()

    def collision(self, opponent):
        from CyberSheep import CyberSheep
        if not isinstance(opponent, CyberSheep):
            self.getWorld().addInfo(self.getName() + " zabił " + opponent.getName() + " na polu " + str(opponent.getXPos()) + " " + str(opponent.getYPos()) + "\n")
            opponent.setAlive(False)
            self.setAlive(False)