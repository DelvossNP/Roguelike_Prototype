# run this program with python 3
import numpy as np
import random
import tkinter as tk
from PIL import ImageTk, Image
import time

from classes import *
from dungeon_generation import *
from player_interaction import *
from dictionaries import *
from actions import *
from UI import *


# initializes the window in which the game is played
window = tk.Tk()
window.title("Roguelike_Prototype")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.overrideredirect(1)
window.geometry("%dx%d+0+0" % (w, h))
window.configure(background='grey')


def init_level(img, window):

    # new level is generated via these 3 lines
    # from set image creates the array which contains all the level information
    # the array is then used to create the GUI and all the enemy/item objects and their respective dictionaries
    playing_field, m, n = dungeon_gen(img)
    wall_1, floor_1, player_1, rats, orcs, ghosts, swords, potions, stairs_1 = create_GUI(playing_field, m, n, window)
    # enemy/item objects can be accessed simply by their positions in the array via the following dictionaries
    enemies, items, map_objects = create_dictionaries(rats, orcs, ghosts, swords, potions, stairs_1)
    # apparently binding again is necessary because the playing_field argument doesn't automatically get updated from the old one
    window.bind("<Button-1>", lambda event, arg=playing_field: callback(event, arg))
    return(playing_field, m, n, wall_1, floor_1, player_1, rats, orcs, ghosts, swords, potions, stairs_1, enemies, items, map_objects)


playing_field, m, n, wall_1, floor_1, player_1, rats, orcs, ghosts, swords, potions, stairs_1, enemies, items, map_objects = init_level("images\level_1.png", window)

# creates and initializes the UI (player health, etc) and the monster info panels
info_monster_img, info_monster_name, info_monster_hp, info_monster_hp_value, info_monster_damage, info_monster_damage_value = init_monster_info(m)
img_hp, img_hp_bar, img_mana, img_mana_bar = init_UI_images()
player_hp_value_label, player_mana_value_label, player_damage_value_label, exit_game_button = init_UI(img_hp, img_hp_bar, img_mana, img_mana_bar, player_1, m, window)


# the following two functions are responsible for processing keyboard and mouse input from the player
def key(event):

    global wasd
    wasd = repr(event.char)

def callback(event, playing_field):
    grid_info = event.widget.grid_info()
    grid_location_x = grid_info["column"]
    grid_location_y = grid_info["row"]
    m = len(playing_field)

    if 1000 < playing_field[grid_location_y, grid_location_x] < 2000:
        click_info(enemies, m, grid_location_y, grid_location_x, False,
        info_monster_img, info_monster_name, info_monster_hp, info_monster_hp_value, info_monster_damage, info_monster_damage_value)

    elif playing_field[grid_location_y, grid_location_x] == 1 or playing_field[grid_location_y, grid_location_x] == 0:
        click_info(enemies, m, grid_location_y, grid_location_x, True,
        info_monster_img, info_monster_name, info_monster_hp, info_monster_hp_value, info_monster_damage, info_monster_damage_value)

# here, key() and callback() are connected to key and mouse presses respectively, playing_field is passed as an additional argument to callback (see player_interaction.py)
wasd = window.bind("<Key>", key)
# window.bind("<Button-1>", lambda event, arg=playing_field: callback(event, arg))


# Main game loop performs move input (either None or w/a/s/d) and everything following from a move, also checks for game over via player health
def main_game_loop(items, enemies, map_objects, player_1, floor_1, window, playing_field, player_hp_value_label, player_damage_value_label):

    global wasd

    while True:

        player_1, player_1.pos_x, player_1.pos_y, level_exit = move(wasd, items, enemies, map_objects, player_1, floor_1, player_1.pos_x, player_1.pos_y, player_1.damage,
                                                        window, playing_field, player_hp_value_label, player_damage_value_label)
        if player_1.health <= 0:
            exit_game("You have died!", window)
            raise SystemExit

        if level_exit == True:
            break

        wasd = "0"
        window.update()
    return(player_1)

main_game_loop(items, enemies, map_objects, player_1, floor_1, window, playing_field, player_hp_value_label, player_damage_value_label)

playing_field, m, n, wall_1, floor_1, player_1, rats, orcs, ghosts, swords, potions, stairs_1, enemies, items, map_objects = init_level("images\level_2.png", window)
main_game_loop(items, enemies, map_objects, player_1, floor_1, window, playing_field, player_hp_value_label, player_damage_value_label)

raise SystemExit
