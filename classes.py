from PIL import ImageTk, Image

class floor:

    def __init__(self):
        self.img = ImageTk.PhotoImage(Image.open("images\white.png"))

class wall:

    def __init__(self):
        self.img = ImageTk.PhotoImage(Image.open("images\wall.png"))

class player:

    def __init__(self, pos_x, pos_y):
        self.name = "Player"
        self.img = ImageTk.PhotoImage(Image.open("images\player.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 100
        self.damage = 50

class rat:

    def __init__(self, pos_x, pos_y):
        self.name = "Rat"
        self.img = ImageTk.PhotoImage(Image.open("images\\rat.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 70
        self.damage = 20

class orc:

    def __init__(self, pos_x, pos_y):
        self.name = "Orc"
        self.img = ImageTk.PhotoImage(Image.open("images\orc.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 150
        self.damage = 35

class ghost:

    def __init__(self, pos_x, pos_y):
        self.name = "Ghost"
        self.img = ImageTk.PhotoImage(Image.open("images\ghost.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 120
        self.damage = 50

class sword:

    def __init__(self, pos_x, pos_y):
        self.name = "Sword"
        self.img = ImageTk.PhotoImage(Image.open("images\sword.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 0
        self.damage = 20

class potion:

    def __init__(self, pos_x, pos_y):
        self.name = "Potion"
        self.img = ImageTk.PhotoImage(Image.open("images\potion.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 50
        self.damage = 0

<<<<<<< HEAD
=======

>>>>>>> 1fd88093822bbfe07ad1a8f217d4f9cbfdec1747
class stairs:

    def __init__(self, pos_x, pos_y):
        self.name = "Stairs"
        self.img = ImageTk.PhotoImage(Image.open("images\player.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
<<<<<<< HEAD
=======


# add new enemy guide:
#
# 1. add new class for new enemy (classes.py)
#
# 2. add new dictionary for new enemy and add it to the taken arguments of create_dictionaries (dictionaries.py)
#
# 3. add new enemy to color map (dungeon_generation.py)
#
# 4. add new list for new enemy, new elif and return variable in create_GUI (dungeon_generation.py)
#
# 5. add new enemy to object creation and dictionary connection(main.py)
>>>>>>> 1fd88093822bbfe07ad1a8f217d4f9cbfdec1747
