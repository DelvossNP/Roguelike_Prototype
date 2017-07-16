from dungeon_generation import geometry_placer
import tkinter as tk

def move(wasd, items, enemies, player_1, floor_1, player_pos_x, player_pos_y, player_damage, window, playing_field, player_hp_value_label, player_damage_value_label):

    wasd = str(wasd)
    player_pos_x_old = player_pos_x
    player_pos_y_old = player_pos_y
    playing_field[player_pos_y, player_pos_x] = 1
    m = len(playing_field)

    if wasd == "'w'" or wasd == "'W'":
        player_pos_y -= 1

    elif wasd == "'a'" or wasd == "'A'":
        player_pos_x -= 1

    elif wasd == "'s'" or wasd == "'S'":
        player_pos_y += 1

    elif wasd == "'d'" or wasd == "'D'":
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
        player_pos_y, player_pos_x, player_pos_y_old, player_pos_x_old, playing_field, window, m, player_hp_value_label)
        return(player_1, player_pos_x, player_pos_y)

    elif 2000 < playing_field[player_pos_y, player_pos_x] < 3000:
        playing_field[player_pos_y, player_pos_x] = 9
        geometry_placer(player_1.img, player_pos_x, player_pos_y, window)
        geometry_placer(floor_1.img, player_pos_x_old, player_pos_y_old, window)
        pick_up_item(items, player_1, player_pos_y, player_pos_x, m, player_hp_value_label, player_damage_value_label)
        return(player_1, player_pos_x, player_pos_y)

    else:
        playing_field[player_pos_y, player_pos_x] = 9
        geometry_placer(player_1.img, player_pos_x, player_pos_y, window)
        geometry_placer(floor_1.img, player_pos_x_old, player_pos_y_old, window)
        return(player_1, player_pos_x, player_pos_y)


def pick_up_item(items, player_1, player_pos_y, player_pos_x, m, player_hp_value_label, player_damage_value_label):
    player_1.damage += items[(player_pos_y, player_pos_x)].damage
    player_1.health += items[(player_pos_y, player_pos_x)].health

    player_hp_value_label.config(text = (str(player_1.health)))
    player_damage_value_label.config(text = (str(player_1.damage)))


def fight(player_1, enemies, floor_1, player_pos_y, player_pos_x, player_pos_y_old, player_pos_x_old, playing_field, window, m, player_hp_value_label):

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

    player_hp_value_label.config(text = (str(player_1.health)))

    player_pos_x = player_pos_x_old
    player_pos_y = player_pos_y_old
    playing_field[player_pos_y, player_pos_x] = 9
    return(player_1, player_pos_x, player_pos_y, playing_field)
