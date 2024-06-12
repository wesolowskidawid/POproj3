from Plant import Plant

class Sonchus(Plant):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 0, 0, xPos, yPos, "Sonchus", "Mlecz")
        self.setImage("Sonchus.png")

    def collision(self, opponent):
        # info
        self.setAlive(False)