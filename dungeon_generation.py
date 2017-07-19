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

    # enemies are indicated in the main array via numbers ranging from 1001 (rat) up to 1999
    # items are indicated in the main array via numbers ranging from 2001 to 2999
    colors_map = {
            (255, 255, 255): 1,
            (0, 0, 0): 0,
            (0, 0, 255): 9,
            (255, 0, 0): 1001,
            (254, 0, 0): 1002,
            (253, 0, 0): 1003,
            (0, 255, 0): 2001,
            (0, 254, 0): 2002,
            (0, 0, 254): 3001,
            }

    for i in range(0, m):
        for j in range (0, n):
            playing_field[i, j] = (colors_map[pix[j,i]])

    return(playing_field, m, n)


def geometry_placer(img, x, y, window):


    panel = tk.Label(window, highlightthickness = 0, borderwidth = 0, image = img)
    panel.grid(row=y,column=x)

def create_GUI(playing_field, m, n, window):

    rats_exist = False
    orcs_exist = False
    ghosts_exist = False
    swords_exist = False
    potions_exist = False
    floor_1 = floor()
    wall_1 = wall()

    for i in range(0, m):
        for j in range(0, n):
            if playing_field[i][j] == 0:
                geometry_placer(wall_1.img, j, i, window)

            elif playing_field[i][j] == 1:
                geometry_placer(floor_1.img, j, i, window)

            elif playing_field[i][j] == 9:
                if not ("player_1" in locals()):
                    player_1 = player(j, i)
                else:
                    player_1.pos_x = j
                    player_1.pos_y = i
                geometry_placer(player_1.img, j, i, window)

            elif playing_field[i][j] == 1001:
                if rats_exist == False:
                    rats = []
                    rats_exist = True
                rats.append(rat(j, i))
                geometry_placer(rats[0].img, j, i, window)

            elif playing_field[i][j] == 1002:
                if orcs_exist == False:
                    orcs = []
                    orcs_exist = True
                orcs.append(orc(j, i))
                geometry_placer(orcs[0].img, j, i, window)

            elif playing_field[i][j] == 1003:
                if ghosts_exist == False:
                    ghosts = []
                    ghosts_exist = True
                ghosts.append(ghost(j, i))
                geometry_placer(ghosts[0].img, j, i, window)

            elif playing_field[i][j] == 2001:
                if swords_exist == False:
                    swords = []
                    swords_exist = True
                swords.append(sword(j, i))
                geometry_placer(swords[0].img, j, i, window)

            elif playing_field[i][j] == 2002:
                if potions_exist == False:
                    potions = []
                    potions_exist = True
                potions.append(potion(j, i))
                geometry_placer(potions[0].img, j, i, window)

            elif playing_field[i][j] == 3001:
                stairs_1 = stairs(j, i)
                geometry_placer(stairs_1.img, j, i, window)

    return(wall_1, floor_1, player_1, rats, orcs, ghosts, swords, potions, stairs_1)
