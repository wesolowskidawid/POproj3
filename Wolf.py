from Animal import Animal

class Wolf(Animal):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 9, 5, xPos, yPos, "Wolf", "Wilk")
        self.setImage("Wolf.png")

