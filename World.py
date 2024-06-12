import random
import tkinter as tk
from tkinter import filedialog
import os
from Human import Human
from Antelope import Antelope
from Belladonna import Belladonna
from CyberSheep import CyberSheep
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from Hogweed import Hogweed
from Sheep import Sheep
from Sonchus import Sonchus
from Turtle import Turtle
from Wolf import Wolf
from PIL import Image, ImageTk


class World:
    def __init__(self, width=10, height=10, filename=None):
        self.__width = width
        self.__height = height
        self.organisms = []
        self.newOrganisms = []
        self.turn = 0
        self.human = None
        self.canMove = True
        self.image_tks = {}
        self.info = ""

        self.root = tk.Tk()
        self.root.title("Symulator Świata")

        self.canvas = tk.Canvas(self.root, width=width * 20 + 20, height=height * 20 + 20, bg='white')
        self.canvas.pack()

        self.world_info = tk.Label(self.root, text="", anchor='w', justify='left')
        self.world_info.pack(fill='x')

        self.general_frame = tk.Frame(self.root)
        self.general_frame.pack(side='left', padx=10)

        self.general_info = tk.Label(self.general_frame, text="", anchor='w', justify='left')
        self.general_info.pack(fill='x')

        self.root.bind('<Return>', self.update_gui)
        self.root.bind('s', self.save_to_file)
        self.root.bind('<space>', self.usePlayerSpecialAbility)
        self.root.bind('<Left>', lambda event: self.movePlayer(event, -1, 0))
        self.root.bind('<Right>', lambda event: self.movePlayer(event, 1, 0))
        self.root.bind('<Up>', lambda event: self.movePlayer(event, 0, -1))
        self.root.bind('<Down>', lambda event: self.movePlayer(event, 0, 1))
        self.canvas.bind("<Button-1>", self.show_context_menu)

        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Dodaj organizm", command=self.add_animal_dialog)

        if filename:
            self.load_from_file(filename)

    def show_context_menu(self, event):
        self.context_menu.post(event.x_root, event.y_root)
        self.clicked_x = event.x // 20
        self.clicked_y = event.y // 20

    def add_animal_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Choose an animal")

        label = tk.Label(dialog, text="Choose an animal:")
        label.pack(pady=10)

        animal_var = tk.StringVar(dialog)
        animal_var.set("Antelope")  # Default value

        options = [
            "Antelope", "Belladonna", "CyberSheep", "Fox", "Grass", "Guarana",
            "Hogweed", "Sheep", "Sonchus", "Turtle", "Wolf"
        ]
        dropdown = tk.OptionMenu(dialog, animal_var, *options)
        dropdown.pack(pady=10)

        button = tk.Button(dialog, text="Add", command=lambda: self.add_animal(animal_var.get(), dialog))
        button.pack(pady=10)

    def add_animal(self, species, dialog):
        x, y = self.clicked_x, self.clicked_y
        organism = self.createOrganism(species, x, y)
        if organism:
            self.addOrganism(organism)
            self.load_image(organism)
            if self.newOrganisms:
                self.organisms.extend(self.newOrganisms)
                self.newOrganisms = []
            self.printBoard()
        dialog.destroy()

    def usePlayerSpecialAbility(self, event=None):
        if self.human.isAlive() and not self.human.isSpecialAbilityActive() and self.human.getSpecialAbilityCooldown() == 0:
            self.human.useSpecialAbility()
            self.world_info.config(text=self.info)

    def movePlayer(self, event=None, x=0, y=0):
        if self.human.isAlive() and self.canMove:
            self.canMove = False
            self.human.move(x, y)
            if self.getOrganism(self.human.getXPos(), self.human.getYPos()) is not None:
                self.human.collision(self.getOrganism(self.human.getXPos(), self.human.getYPos()))
                self.world_info.config(text=self.info)
            self.printBoard()

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

            width = int(lines[0].split(': ')[1])
            height = int(lines[1].split(': ')[1])
            self.setWidth(width)
            self.setHeight(height)

            turn = int(lines[2].split(': ')[1])
            self.turn = turn

            human_info_index = 4
            if "Position:" in lines[human_info_index + 1]:
                human_info = lines[human_info_index + 1]
                human_pos = human_info.split(': ')[1].strip('()\n').split(', ')
                human_x = int(human_pos[0])
                human_y = int(human_pos[1])
                self.human = Human(self, human_x, human_y)
                self.load_image(self.human)
                self.human.setAge(int(lines[human_info_index + 2].split(': ')[1]))
                self.human.setSpecialAbilityActive(lines[human_info_index + 3].split(': ')[1].strip() == 'True')
                self.human.setSpecialAbilityCooldown(int(lines[human_info_index + 4].split(': ')[1]))
                self.human.setSpecialAbilityDuration(int(lines[human_info_index + 5].split(': ')[1]))

            self.organisms = []
            organisms_section = False
            for line in lines:
                if organisms_section:
                    if line.strip():
                        if line.strip() == "Organisms:":
                            continue
                        species = line.split(': ')[1].strip('\n')
                        pos_line_index = lines.index(line) + 1
                        if pos_line_index < len(lines):
                            pos_line = lines[pos_line_index]
                            if "Position:" in pos_line:
                                pos = pos_line.split(': ')[1].strip('()\n').split(', ')
                                x = int(pos[0])
                                y = int(pos[1])
                                age_line = lines[pos_line_index + 1]
                                strength_line = lines[pos_line_index + 2]
                                initiative_line = lines[pos_line_index + 3]
                                breeding_cooldown_line = lines[pos_line_index + 4]
                                age = int(age_line.split(': ')[1])
                                strength = int(strength_line.split(': ')[1])
                                initiative = int(initiative_line.split(': ')[1])
                                breeding_cooldown = int(breeding_cooldown_line.split(': ')[1])
                                organism = self.createOrganism(species, x, y)
                                organism.setAge(age)
                                organism.setStrength(strength)
                                organism.setInitiative(initiative)
                                organism.setBreedingCooldown(breeding_cooldown)
                                self.organisms.append(organism)
                                self.load_image(organism)
                elif line.strip() == "Organisms:":
                    organisms_section = True

            if not self.organisms:
                print("Nieprawidłowe lub brak danych dotyczących organizmów.")

    def save_to_file(self, event=None):
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        with open(filename, 'w') as file:
            file.write(f"Width: {self.__width}\n")
            file.write(f"Height: {self.__height}\n")
            file.write(f"Turn: {self.turn}\n\n")
            file.write("Human:\n")
            file.write(f"Position: ({self.human.getXPos()}, {self.human.getYPos()})\n")
            file.write(f"Age: {self.human.getAge()}\n")
            file.write(f"Special Ability Active: {self.human.isSpecialAbilityActive()}\n")
            file.write(f"Special Ability Cooldown: {self.human.getSpecialAbilityCooldown()}\n")
            file.write(f"Special Ability Duration: {self.human.getSpecialAbilityDuration()}\n\n")

            file.write("Organisms:\n")
            for organism in self.organisms:
                file.write(f"Species: {organism.getSpecies()}\n")
                file.write(f"Position: ({organism.getXPos()}, {organism.getYPos()})\n")
                file.write(f"Age: {organism.getAge()}\n")
                file.write(f"Strength: {organism.getStrength()}\n")
                file.write(f"Initiative: {organism.getInitiative()}\n")
                file.write(f"Breeding Cooldown: {organism.getBreedingCooldown()}\n\n")

    def create_organisms(self):
        maxOrganisms = int(self.__width * self.__height / 100 + 1)

        hw = random.randint(0, self.__width - 1)
        hh = random.randint(0, self.__height - 1)
        self.human = Human(self, hw, hh)
        self.load_image(self.human)

        n = random.randint(1, maxOrganisms)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Antelope(self, x, y)
            self.load_image(o)
            self.organisms.append(o)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Belladonna(self, x, y)
            self.load_image(o)
            self.organisms.append(o)
        # for i in range(n):
        #     x = random.randint(0, self.__width - 1)
        #     y = random.randint(0, self.__height - 1)
        #     if self.getOrganism(x, y) is not None:
        #         continue
        #     o = CyberSheep(self, x, y)
        #     self.load_image(o)
        #     self.organisms.append(o)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Fox(self, x, y)
            self.load_image(o)
            self.organisms.append(o)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Grass(self, x, y)
            self.load_image(o)
            self.organisms.append(o)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Guarana(self, x, y)
            self.load_image(o)
            self.organisms.append(o)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Hogweed(self, x, y)
            self.load_image(o)
            self.organisms.append(o)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Sheep(self, x, y)
            self.load_image(o)
            self.organisms.append(o)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Sonchus(self, x, y)
            self.load_image(o)
            self.organisms.append(o)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Turtle(self, x, y)
            self.load_image(o)
            self.organisms.append(o)
        for i in range(n):
            x = random.randint(0, self.__width - 1)
            y = random.randint(0, self.__height - 1)
            if self.getOrganism(x, y) is not None:
                continue
            o = Wolf(self, x, y)
            self.load_image(o)
            self.organisms.append(o)

    def load_image(self, organism):
        image_path = os.path.join(os.path.dirname(__file__), 'assets', organism.getImage())
        image_pil = Image.open(image_path)
        image_resized = image_pil.resize((20, 20))
        image_tk = ImageTk.PhotoImage(image_resized)
        self.image_tks[organism] = image_tk

    def update_gui(self, event=None):
        self.canMove = True
        self.clearInfo()
        self.turn += 1
        print(f"Turn: {self.turn}")

        if self.newOrganisms:
            self.organisms.extend(self.newOrganisms)
            self.newOrganisms = []

        # print board
        self.printBoard()

        # sort organisms by initiative in descending order
        self.organisms.sort(key=lambda x: x.getInitiative(), reverse=True)

        for organism in self.organisms:
            organism.action()

            # remove dead organisms
            if not organism.isAlive():
                self.organisms.remove(organism)

        for organism in self.organisms:
            organism.increaseAge()
            if organism.getBreedingCooldown() > 0:
                organism.decreaseBreedingCooldown()

        if self.human:
            if self.human.isAlive():
                self.human.increaseAge()

            if self.human.isSpecialAbilityActive():
                self.human.decreaseSpecialAbilityDuration()
                if self.human.getSpecialAbilityDuration() == 0:
                    self.human.setSpecialAbilityActive(False)
                    self.human.setSpecialAbilityCooldown(self.human.getSpecialAbilityCooldownMax())
                else:
                    self.human.decreaseSpecialAbilityCooldown()
            else:
                self.human.decreaseSpecialAbilityCooldown()

        if self.newOrganisms:
            self.organisms.extend(self.newOrganisms)
            self.newOrganisms = []

        general_info_text = ""
        general_info_text += "Dawid Wesolowski 197943\n"
        general_info_text += f"Tura: {self.turn}\n"
        if self.human.isAlive():
            general_info_text += "Poruszaj sie strzalkami\n"
            if self.human.isSpecialAbilityActive():
                general_info_text += f"Superumiejetnosc aktywna: {self.human.getSpecialAbilityDuration()} tur\n"
            elif self.human.isSpecialAbilityActive() == False and self.human.getSpecialAbilityCooldown() > 0:
                general_info_text += f"Superumiejetnosc niedostepna: {self.human.getSpecialAbilityCooldown()} tur\n"
            else:
                general_info_text += "Aktywuj superumiejetnosc wciskajac 'Spacja'\n"
        general_info_text += "Zapisz gre wciskajac 's'\n"

        self.world_info.config(text=self.info)
        self.general_info.config(text=general_info_text)

        self.printBoard()

    def run(self):
        self.root.mainloop()

    def addOrganism(self, organism):
        self.newOrganisms.append(organism)
        self.load_image(organism)

    def getOrganism(self, x, y):
        for organism in self.organisms:
            if organism.getXPos() == x and organism.getYPos() == y:
                return organism

        return None

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width
        self.canvas.config(width=width * 20 + 20)

    def addInfo(self, info):
        self.info += info + "\n"

    def clearInfo(self):
        self.info = ""

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height
        self.canvas.config(height=height * 20 + 20)

    def createOrganism(self, species, x, y):
        if species == "Antelope":
            return Antelope(self, x, y)
        elif species == "Belladonna":
            return Belladonna(self, x, y)
        elif species == "CyberSheep":
            return CyberSheep(self, x, y)
        elif species == "Fox":
            return Fox(self, x, y)
        elif species == "Grass":
            return Grass(self, x, y)
        elif species == "Guarana":
            return Guarana(self, x, y)
        elif species == "Hogweed":
            return Hogweed(self, x, y)
        elif species == "Sheep":
            return Sheep(self, x, y)
        elif species == "Sonchus":
            return Sonchus(self, x, y)
        elif species == "Turtle":
            return Turtle(self, x, y)
        elif species == "Wolf":
            return Wolf(self, x, y)
        else:
            return None

    def printBoard(self):
        self.canvas.delete("all")
        for i in range(self.__width):
            for j in range(self.__height):
                self.canvas.create_rectangle(i * 20, j * 20, i * 20 + 20, j * 20 + 20, fill='white', outline='black')
        if self.human.isAlive():
            image_tk = self.image_tks[self.human]
            self.canvas.create_image(self.human.getXPos() * 20, self.human.getYPos() * 20, image=image_tk, anchor='nw')
        for organism in self.organisms:
            x = organism.getXPos() * 20
            y = organism.getYPos() * 20
            image_tk = self.image_tks[organism]
            self.canvas.create_image(x, y, image=image_tk, anchor='nw')
