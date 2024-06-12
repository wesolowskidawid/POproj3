import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import filedialog
from World import World

firstChoice = None
width = 20
height = 20

def new_world():
    global firstChoice
    firstChoice = 'new'

    width = simpledialog.askinteger("Szerokość", "Podaj szerokość świata", minvalue=5, maxvalue=50)
    height = simpledialog.askinteger("Wysokość", "Podaj wysokość świata", minvalue=5, maxvalue=30)

    if width and height:
        global world_width, world_height
        world_width = width
        world_height = height
        root.destroy()

def load_world():
    global firstChoice
    firstChoice = 'load'
    root.destroy()

def exit_game():
    global firstChoice
    firstChoice = 'exit'
    root.destroy()


root = tk.Tk()
root.title("Symulator Świata")

new_button = tk.Button(root, text="Nowa gra", command=new_world)
new_button.pack(pady=10)

load_button = tk.Button(root, text="Wczytaj grę", command=load_world)
load_button.pack(pady=10)

exit_button = tk.Button(root, text="Wyjdź", command=exit_game)
exit_button.pack(pady=10)

root.mainloop()

if firstChoice == 'exit':
    exit()
elif firstChoice == 'load':
    filename = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    world = World(filename=filename)
    world.run()
elif firstChoice == 'new':
    world = World(world_width, world_height)
    world.create_organisms()
    world.run()
