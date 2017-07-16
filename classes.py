from PIL import ImageTk, Image

class floor:

    def __init__(self):
        self.img = ImageTk.PhotoImage(Image.open("white.png"))

class wall:

    def __init__(self):
        self.img = ImageTk.PhotoImage(Image.open("black.png"))

class player:

    def __init__(self, pos_x, pos_y):
        self.name = "Player"
        self.img = ImageTk.PhotoImage(Image.open("player.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 100
        self.damage = 50

class rat:

    def __init__(self, pos_x, pos_y):
        self.name = "Rat"
        self.img = ImageTk.PhotoImage(Image.open("rat.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 70
        self.damage = 20

class orc:

    def __init__(self, pos_x, pos_y):
        self.name = "Orc"
        self.img = ImageTk.PhotoImage(Image.open("orc.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 150
        self.damage = 35

class sword:

    def __init__(self, pos_x, pos_y):
        self.name = "Sword"
        self.img = ImageTk.PhotoImage(Image.open("sword.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 0
        self.damage = 20

class potion:

    def __init__(self, pos_x, pos_y):
        self.name = "Potion"
        self.img = ImageTk.PhotoImage(Image.open("potion.png"))
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = 50
        self.damage = 0
