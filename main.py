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

#TODO: possible to shorten actions.py function move parameters because the whole object player_1 is passed? Thus, no need to pass parameters which belong to this object
#TODO: guide on how to add new enemies, items (later skills and dungeon-levels)

# enemies are indicated in the main array via numbers ranging from 1001 (rat) up to 1999
# items are indicated in the main array via numbers ranging from 2001 to 299

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

window = tk.Tk()
window.title("Gamelike")
window.geometry("1160x1000")
window.configure(background='grey')

playing_field, m, n = dungeon_gen("rgb_test3.png")
wall_1, floor_1, player_1, rats, orcs, swords, potions = create_playing_field(playing_field, m, n, window)

info_monster_img, info_monster_name, info_monster_hp, info_monster_hp_value, info_monster_damage, info_monster_damage_value = init_monster_info(m)

wasd = window.bind("<Key>", key)
window.bind("<Button-1>", lambda event, arg=playing_field: callback(event, arg))

enemies, items = create_dictionaries(rats, orcs, swords, potions)

player_hp_value_label, player_mana_value_label, player_damage_value_label = init_UI(player_1, m)

window.update()

wasd = "0"

while True:

    (player_1, player_1.pos_x, player_1.pos_y) = move(wasd, items, enemies, player_1, floor_1, player_1.pos_x, player_1.pos_y, player_1.damage,
                                                        window, playing_field, player_hp_value_label, player_damage_value_label)
    if player_1.health <= 0:
        print("Game Over suckerrr")
        raise SystemExit
    wasd = "0"
    window.update()
