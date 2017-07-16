import tkinter as tk

def init_monster_info(m):

    info_monster_img = tk.Label(text = "", bg = "grey")
    info_monster_img.grid(row=5,column=m)
    info_monster_name = tk.Label(text = "", bg = "grey")
    info_monster_name.grid(row = 5, column = m + 1)
    info_monster_hp = tk.Label(text = "", bg = "grey")
    info_monster_hp.grid(row = 6, column = m)
    info_monster_hp_value = tk.Label(text = "", bg = "grey")
    info_monster_hp_value.grid(row = 6, column = m + 1)
    info_monster_damage = tk.Label(text = "", bg = "grey")
    info_monster_damage.grid(row = 7, column = m)
    info_monster_damage_value = tk.Label(text = "", bg = "grey")
    info_monster_damage_value.grid(row = 7, column = m + 1)

    return(info_monster_img, info_monster_name, info_monster_hp, info_monster_hp_value, info_monster_damage, info_monster_damage_value)

# def key(event):
#
#     global wasd
#     wasd = repr(event.char)
#
# def callback(event, playing_field):
#     grid_info = event.widget.grid_info()
#     grid_location_x = grid_info["column"]
#     grid_location_y = grid_info["row"]
#
#     if 1000 < playing_field[grid_location_y, grid_location_x] < 2000:
#         click_info(grid_location_y, grid_location_x,False)
#     elif playing_field[grid_location_y, grid_location_x] == 1 or playing_field[grid_location_y, grid_location_x] == 0:
#         click_info(grid_location_y, grid_location_x,True)
#
def click_info(enemies, m, grid_location_y, grid_location_x, is_floor,
                info_monster_img, info_monster_name, info_monster_hp, info_monster_hp_value, info_monster_damage, info_monster_damage_value):

    if is_floor == False:

        info_monster_img.config(highlightthickness = 0, borderwidth = 0, image = enemies[(grid_location_y, grid_location_x)].img)

        info_monster_name.config(text = enemies[(grid_location_y, grid_location_x)].name , bg="white",
            font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0)

        info_monster_hp.config(text = "HP", bg="orange",
            font = ("Arial", 9), height=2, width = 7, borderwidth = 0, highlightthickness = 0)

        info_monster_hp_value.config(text = enemies[(grid_location_y, grid_location_x)].health,
            bg="green", font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0)

        info_monster_damage.config(text = "Damage",
            bg="orange",  font = ("Arial", 9), height=2, width = 7, borderwidth = 0, highlightthickness = 0)

        info_monster_damage_value.config(text = enemies[(grid_location_y, grid_location_x)].damage,
            bg="red", font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0)

    if is_floor == True:
        click_info_empty(info_monster_img, info_monster_name, info_monster_hp, info_monster_hp_value, info_monster_damage, info_monster_damage_value)


def click_info_empty(info_monster_img, info_monster_name, info_monster_hp, info_monster_hp_value, info_monster_damage, info_monster_damage_value):

    info_monster_img.config(text = "", bg = "grey", image = None)
    info_monster_name.config(text = "", bg = "grey")
    info_monster_hp.config(text = "", bg = "grey")
    info_monster_hp_value.config(text = "", bg = "grey")
    info_monster_damage.config(text = "", bg = "grey")
    info_monster_damage_value.config(text = "", bg = "grey")
