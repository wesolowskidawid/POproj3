from Plant import Plant

class Guarana(Plant):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 0, 0, xPos, yPos, "Guarana", "Guarana")
        self.setImage("Guarana.png")

    def collision(self, opponent):
        # info
        opponent.setStrength(opponent.getStrength() + 3)
        self.setAlive(False)

