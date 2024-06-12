from Animal import Animal
import random


class Human(Animal):
    def __init__(self, world, xPos, yPos):
        super().__init__(world, 5, 4, xPos, yPos, "Human", "Człowiek")
        self.specialAbilityActive = False
        self.specialAbilityCooldown = 0
        self.specialAbilityDuration = 0
        self.specialAbilityCooldownMax = 5
        self.specialAbilityDurationMax = 5
        self.setImage("Steve.png")

    def action(self):
        pass

    def collision(self, opponent):
        if self.isSpecialAbilityActive():
            direction = random.randint(0, 3)
            if direction == 0:
                opponent.move(0, 1)
            elif direction == 1:
                opponent.move(0, -1)
            elif direction == 2:
                opponent.move(1, 0)
            elif direction == 3:
                opponent.move(-1, 0)
            self.getWorld().addInfo(self.getName() + " blokuje atak " + opponent.getName() + " dzieki superumiejetnosci na polu " + str(opponent.getXPos()) + " " + str(opponent.getYPos()) + "\n")
        else:
            super().collision(opponent)

    def getSpecialAbilityCooldown(self):
        return self.specialAbilityCooldown

    def getSpecialAbilityDuration(self):
        return self.specialAbilityDuration

    def isSpecialAbilityActive(self):
        return self.specialAbilityActive

    def useSpecialAbility(self):
        self.getWorld().addInfo(self.getName() + " używa superumiejętności\n")
        self.specialAbilityActive = True
        self.specialAbilityDuration = self.specialAbilityDurationMax

    def decreaseSpecialAbilityCooldown(self):
        if self.specialAbilityCooldown > 0:
            self.specialAbilityCooldown -= 1

    def decreaseSpecialAbilityDuration(self):
        if self.specialAbilityDuration > 0:
            self.specialAbilityDuration -= 1

    def setSpecialAbilityCooldown(self, cooldown):
        self.specialAbilityCooldown = cooldown

    def setSpecialAbilityDuration(self, duration):
        self.specialAbilityDuration = duration

    def setSpecialAbilityActive(self, active):
        self.specialAbilityActive = active

    def getSpecialAbilityCooldownMax(self):
        return self.specialAbilityCooldownMax

    def getSpecialAbilityDurationMax(self):
        return self.specialAbilityDurationMax

