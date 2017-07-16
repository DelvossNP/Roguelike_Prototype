import tkinter as tk

def init_UI(player_1, m):

    tk.Label(text = "HP", bg="orange",  font = ("Arial", 9), height=2, width = 7, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = m)
    tk.Label(text = (str(player_1.health)), bg="green", font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = m + 1)
    tk.Label(text = "Mana", bg="orange",  font = ("Arial", 9), height=2, width = 7, borderwidth = 0, highlightthickness = 0).grid(row = 2, column = m)
    tk.Label(text = "5 / 5", bg="dodgerblue", font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0).grid(row = 2, column = m + 1)
    tk.Label(text = "Damage", bg="orange",  font = ("Arial", 9), height=2, width = 7, borderwidth = 0, highlightthickness = 0).grid(row = 3, column = m)
    tk.Label(text = (str(player_1.damage)), bg="red", font = ("Arial", 9), height=2, width = 20, borderwidth = 0, highlightthickness = 0).grid(row = 3, column = m + 1)
