from Plant import Plant

class Belladonna(Plant):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 99, 0, xPos, yPos, "Belladonna", "Wilcza jagoda")
        self.setImage("Belladonna.png")

    def collision(self, opponent):
        self.getWorld().addInfo(self.getName() + " zabił " + opponent.getName() + " na polu " + str(opponent.getXPos()) + " " + str(opponent.getYPos()) + "\n")
        self.setAlive(False);
        opponent.setAlive(False);