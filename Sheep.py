from Animal import Animal

class Sheep(Animal):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 4, 4, xPos, yPos, "Sheep", "Owca")
        self.setImage("Sheep.png")