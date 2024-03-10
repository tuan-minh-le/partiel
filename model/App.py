# -*- coding: utf-8 -*-

"""
 * @author : maxime
 * @email : maxime.barthomeuf@cpe.fr
 * @date : 18/12/2023, lundi
 * TODO :
"""

import tkinter as tk

from view.GameView import GameView
from controller.GameController import GameController


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Game")
        self.geometry("800x600")

        self.resizable(False, False)
        self.configure(background='black')

        self.game_view = GameView(self, self, GameController(self))
        self.game_view.place(x=0, y=0, relheight=1, relwidth=1)
