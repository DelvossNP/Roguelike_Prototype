import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
from classes import *

def dungeon_gen(level_img_name):

    im = Image.open(level_img_name) #Can be many different formats.
    pix = im.load()
    n, m = im.size
    playing_field = np.zeros((m,n))

    playing_field = np.zeros((m , n))

    colors_map = {
            (255, 255, 255): 1,
            (0, 0, 0): 0,
            (0, 0, 255): 9,
            (255, 0, 0): 1001,
            (254, 0, 0): 1002,
            (0, 255, 0): 2001,
            (0, 254, 0): 2002,
            }

    for i in range(0, m):
        for j in range (0, n):
            playing_field[i, j] = (colors_map[pix[j,i]])

    return(playing_field, m, n)


def geometry_placer(img, x, y, window):


    panel = tk.Label(window, highlightthickness = 0, borderwidth = 0, image = img)
    panel.grid(row=y,column=x)

def create_playing_field(playing_field, m, n, window):

    rats = []
    orcs = []
    swords = []
    potions = []
    floor_1 = floor()
    wall_1 = wall()

    for i in range(0, m):
        for j in range(0, n):
            if playing_field[i][j] == 0:
                geometry_placer(wall_1.img, j, i, window)

            elif playing_field[i][j] == 1:
                geometry_placer(floor_1.img, j, i, window)

            elif playing_field[i][j] == 9:
                player_1 = player(j, i)
                geometry_placer(player_1.img, j, i, window)

            elif playing_field[i][j] == 1001:
                rats.append(rat(j, i))
                geometry_placer(rats[0].img, j, i, window)

            elif playing_field[i][j] == 1002:
                orcs.append(orc(j, i))
                geometry_placer(orcs[0].img, j, i, window)

            elif playing_field[i][j] == 2001:
                swords.append(sword(j, i))
                geometry_placer(swords[0].img, j, i, window)

            elif playing_field[i][j] == 2002:
                potions.append(potion(j, i))
                geometry_placer(potions[0].img, j, i, window)

    return(wall_1, floor_1, player_1, rats, orcs, swords, potions)
