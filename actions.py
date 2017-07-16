from dungeon_generation import geometry_placer
import tkinter as tk

def move(wasd, items, enemies, player_1, floor_1, player_pos_x, player_pos_y, player_damage, window, playing_field):

    wasd = str(wasd)
    player_pos_x_old = player_pos_x
    player_pos_y_old = player_pos_y
    playing_field[player_pos_y, player_pos_x] = 1
    m = len(playing_field)

    if wasd == "'w'":
        player_pos_y -= 1

    elif wasd == "'a'":
        player_pos_x -= 1

    elif wasd == "'s'":
        player_pos_y += 1

    elif wasd == "'d'":
        player_pos_x += 1

    elif wasd == "'\\x1b'":
        print("Goodbye :(")
        raise SystemExit

    else:
        return(player_1, player_pos_x, player_pos_y)

    if playing_field[player_pos_y, player_pos_x] == 0:
        player_pos_x = player_pos_x_old
        player_pos_y = player_pos_y_old
        playing_field[player_pos_y, player_pos_x] = 9
        return(player_1, player_pos_x, player_pos_y)

    # monsters are assigned numbers from 1001 to 1999 in the array
    elif 1000 < playing_field[player_pos_y, player_pos_x] < 2000:

        (player_1, player_pos_x, player_pos_y, playing_field) = fight(player_1, enemies, floor_1,
        player_pos_y, player_pos_x, player_pos_y_old, player_pos_x_old, playing_field, window, m)
        return(player_1, player_pos_x, player_pos_y)

    elif 2000 < playing_field[player_pos_y, player_pos_x] < 3000:
        playing_field[player_pos_y, player_pos_x] = 9
        geometry_placer(player_1.img, player_pos_x, player_pos_y, window)
        geometry_placer(floor_1.img, player_pos_x_old, player_pos_y_old, window)
        pick_up_item(items, player_1, player_pos_y, player_pos_x, m)
        return(player_1, player_pos_x, player_pos_y)

    else:
        playing_field[player_pos_y, player_pos_x] = 9
        geometry_placer(player_1.img, player_pos_x, player_pos_y, window)
        geometry_placer(floor_1.img, player_pos_x_old, player_pos_y_old, window)
        return(player_1, player_pos_x, player_pos_y)


def pick_up_item(items, player_1, player_pos_y, player_pos_x, m):
    player_1.damage += items[(player_pos_y, player_pos_x)].damage
    player_1.health += items[(player_pos_y, player_pos_x)].health
    tk.Label(text = (str(player_1.health)), bg="green",
    font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = m + 1)
    tk.Label(text = (str(player_1.damage)), bg="red", font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0).grid(row = 3, column = m + 1)


def fight(player_1, enemies, floor_1, player_pos_y, player_pos_x, player_pos_y_old, player_pos_x_old, playing_field, window, m):

    enemies[(player_pos_y, player_pos_x)].health -= player_1.damage

    if enemies[(player_pos_y, player_pos_x)].health <= 0:
        enemies[(player_pos_y, player_pos_x)].health = 0
        playing_field[player_pos_y, player_pos_x] = 1
        geometry_placer(floor_1.img, player_pos_x, player_pos_y, window)
        player_pos_x = player_pos_x_old
        player_pos_y = player_pos_y_old
        playing_field[player_pos_y, player_pos_x] = 9
        return(player_1, player_pos_x, player_pos_y, playing_field)

    player_1.health -= enemies[(player_pos_y, player_pos_x)].damage
    tk.Label(text = (str(player_1.health)), bg="green",
    font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = m + 1)
    player_pos_x = player_pos_x_old
    player_pos_y = player_pos_y_old
    playing_field[player_pos_y, player_pos_x] = 9
    return(player_1, player_pos_x, player_pos_y, playing_field)
