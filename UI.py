import tkinter as tk
from PIL import ImageTk, Image

def init_UI_images():
    img_hp = ImageTk.PhotoImage(Image.open("images\health.png"))
    img_hp_bar = ImageTk.PhotoImage(Image.open("images\healthbar.png"))
    return(img_hp, img_hp_bar)

def init_UI(img_hp, img_hp_bar, player_1, m, window):

    exit_game_button = tk.Button(text="Exit Game", command=lambda : exit_game("Goodbye :(", window))
    exit_game_button.grid(row=0, column=m, columnspan = 2)

    player_hp_label = tk.Label(highlightthickness = 0, borderwidth = 0, image = img_hp)
    player_hp_label.grid(row=1, column=m)

    player_hp_value_label = tk.Label(highlightthickness = 0, borderwidth = 0, image = img_hp_bar)
    player_hp_value_label.grid(row=1, column=m+1)
    player_hp_value_label = tk.Label(text = (str(player_1.health)), bg="red",
    font = ("Arial", 12), height=1, width = 3, borderwidth = 0, highlightthickness = 0)
    player_hp_value_label.grid(row=1, column = m+1)

    player_mana_label = tk.Label(text = "Mana", bg="orange",
    font = ("Arial", 9), height=2, width = 7, borderwidth = 0, highlightthickness = 0)
    player_mana_label.grid(row = 2, column = m)

    player_mana_value_label = tk.Label(text = "5 / 5", bg="dodgerblue",
    font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0)
    player_mana_value_label.grid(row = 2, column = m + 1)

    player_damage_label = tk.Label(text = "Damage", bg="orange",
    font = ("Arial", 9), height=2, width = 7, borderwidth = 0, highlightthickness = 0)
    player_damage_label.grid(row = 3, column = m)

    player_damage_value_label = tk.Label(text = (str(player_1.damage)), bg="red",
    font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0)
    player_damage_value_label.grid(row = 3, column = m + 1)

    return(player_hp_value_label, player_mana_value_label, player_damage_value_label, exit_game_button)

def exit_game(reason, window):

    print(reason)
    window.destroy()
