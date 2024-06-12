from Plant import Plant

class Grass(Plant):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 0, 0, xPos, yPos, "Grass", "Trawa")
        self.setImage("Grass.png")

    def collision(self, opponent):
        self.getWorld().addInfo(opponent.getName() + " zjadł " + self.getName() + " na polu " + str(opponent.getXPos()) + " " + str(opponent.getYPos()) + "\n")
        self.setAlive(False)

